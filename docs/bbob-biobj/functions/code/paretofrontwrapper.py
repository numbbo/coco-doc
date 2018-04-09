
import numpy as np
#import ctypes # from ctypes import *

#_libmyCfuncs = np.ctypeslib.load_library('libparetofront', '.')
# _libmyCfuncs = ctypes.cdll.LoadLibrary('libparetofront.dll')

#_libmyCfuncs.paretofront.argtypes = [np.ctypeslib.ndpointer(dtype=np.bool),
#                                     np.ctypeslib.ndpointer(dtype=np.double),
#                                     ctypes.c_uint,
#                                     ctypes.c_uint]
#_libmyCfuncs.paretofront.restype  = ctypes.c_void_p


def callParetoFrontOLD(obj, nobj=None, nsample=None):
    obj = np.asarray(obj, dtype=np.double, order='F') # paretofront.c is compatible with MATLAB --> order='F'
    if nobj is None:
        nobj = obj.shape[1]
    if nsample is None:
        nsample = obj.shape[0]
    frontFlag = np.empty(nsample, dtype=np.bool) # prepare the output
    frontFlag[:] = False # BE CAREFUL: it goes wrong if not set to False!
    _libmyCfuncs.paretofront(frontFlag, obj, long(nsample), long(nobj))
    return frontFlag



def callParetoFront(obj, nobj=None, nsample=None):
    """ Returns a numpy array indicating for each
        solution/row in obj whether it is non-dominated
        or not with respect to all other solutions/rows 
        in obj, assuming minimization.
    """
    obj = np.asarray(obj, dtype=np.double)
    if nobj is None:
        nobj = obj.shape[1]
    if nobj > 2:
        raise NotImplementedError('number of objectives too high (>2) for this implementation!')
    if nsample is None:
        nsample = obj.shape[0]

    frontFlag = np.empty(nsample, dtype=np.bool) # prepare the output
    frontFlag[:] = False

    # sort wrt. first objective and
    # store original sorting in idx
    idx = obj[:, 0].argsort()
    objsorted = obj[idx]


    frontFlag[idx[0]] = True
    # store in minftwo the smallest f_2 value of all non-dominated points seen so far:
    minftwo = objsorted[0][1]

    for i in range(1,nsample):
        if objsorted[i][1] < minftwo:
            frontFlag[idx[i]] = True # make sure to store at original (unsorted) entry
            minftwo = objsorted[i][1]

    return frontFlag


# Test case:
# A = np.array([[1,4], [2,2], [4,1], [3,3], [2,3], [3,2], [1.5,3], [5,4], [3,1.5]])
# n = 100; P = np.random.randn(n,2); b = paretofrontwrapper.callParetoFront(P); plt.plot(P[:,0], P[:,1],'o'); plt.plot(P[b,0], P[b,1], 'o', color='red'); plt.show()
