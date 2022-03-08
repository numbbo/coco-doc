"""Usage:

- install the Python modules cocoex and cocopp, see https://github.com/numbbo/coco

- from a shell, call "python listing-1.py", or "run listing-1.py" from IPython/Jupyter

"""
import cocoex, cocopp
from scipy.optimize import fmin_cobyla as fmin
import os, webbrowser  # to open post-processed results in the browser

def get_constraints(problem):
    """return the constraint function from `problem`"""
    def constraint(x):
        """constraints for `fmin_cobyla` where >= 0 means feasible"""
        return -problem.constraint(x)
    return constraint  # a function

suite = cocoex.Suite('bbob-constrained', '', '')
observer = cocoex.Observer('bbob-constrained', 'result_folder: ' + fmin.__name__)
for problem in suite:  # this for-loop takes a minute or two
    problem.observe_with(observer)
    fmin(problem, problem.initial_solution, get_constraints(problem),
         rhobeg=2, rhoend=1e-8, maxfun=1e2)  # next step: increase maxfun to 1e3...

cocopp.main(observer.result_folder)  # post-processing the data, takes two minutes
webbrowser.open("file://" + os.getcwd() + "/ppdata/index.html")  # browse results
