#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#
# Plots the objective space of (random) cuts through the search space
# for the bbob-biobj functions together with some reference sets if available.
#
# Prerequisites:
# * the cocoex module is installed (run `python do.py build-python`)
# * the cocopp module is installed (run `python do.py install-postprocessing`)
#    - choose png and pdf as output format
#    - use in_a_hurry = 0 in genericsettings.py to get the right dpi for the pngs
# * the archive/reference sets are available in the specified folder
#
# based on code by Thanh-Do Tran 2012--2015
# adapted by Dimo Brockhoff 2016--2018

from __future__ import absolute_import, division, print_function, unicode_literals
try: range = xrange  # let range always be an iterator
except NameError: pass
import numpy as np  # "pip install numpy" installs numpy
import cocoex
from cocoex import Suite, Observer, log_level
verbose = 1

import generate_plots



###########################################
# parameters to play with:
dims = (2,3,5,10,20)
functions = range(1,93)  # might take a while...
#functions = (1,2,3,10,20,30,54,55)
instances = (1,2,3)

# Note: in single-objective bbobdocfunctions.pdf documentation, '0' seems to be the instance used
inputfolderforParetoFronts = 'F:/afterBBOB2017/merged_archives_current_data-Jan2018/'
#outputfolder = 'plots/before_workshop/'
tofile = True # if True: files are written; if False: no files but screen output
###########################################


suite_name = "bbob-biobj-ext"
suite_instance = ""
suite_options = "dimensions: 2,3,5,10,20,40"
suite = Suite(suite_name, suite_instance, suite_options)

for problem_index, problem in enumerate(suite):

    f = int(problem.id.lower().split('_f')[1].split('_')[0])
    d = int(problem.id.lower().split('_d')[1].split('_')[0])
    i = int(problem.id.lower().split('_i')[1].split('_')[0])

    #inputfolderforParetoFronts = 'archiveFeb2018/d{0:02d}i{1:02d}/'.format(d,i)
    outputfolder = 'plots/plots-d{0:02d}-i{1:02d}-Feb2018/'.format(d, i)

    f1_id = int(problem.name.lower().split('_f')[1].split('_')[0])
    f2_id = int(problem.name.lower().split('_f')[2].split('_')[0])
    
    i1 = int(problem.name.lower().split('_i')[1].split('_')[0])
    i2 = int(problem.name.lower().split('_i')[2].split('_')[0])
    
    if ((i not in instances) or (f not in functions)
                             or (d not in dims)):
        #print("skipping %s..." % problem.id)
        continue
    else:
        print("processing %s..." % problem.id)
    
    generate_plots.generate_plots(f, d, i, f1_id, f2_id, i1, i2,
                                  outputfolder=outputfolder, 
                                  inputfolder=inputfolderforParetoFronts,
                                  tofile=tofile, downsample=True)