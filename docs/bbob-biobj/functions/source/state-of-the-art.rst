.. _sec:stateoftheart:

===============================================
State-of-the-art in Multiobjective Benchmarking
===============================================


.. todo::

   Write the text of this section. What will go here:

   - state of the art in MO benchmarking, focus on numerical optimization only
   - description of testbeds
   - drawbacks such as distance-based parameters
   
   
.. todo::

   Comment on recommendations and features of test suites as in WFG paper (we kind of have everything but known optima and scalable objectives where the latter is just for now and not in principle)
   
   
.. text by Tobias from March 2016:

  Since the late 1990s, a lot of test function suites for performing comparison between multiobjective optimizers have been proposed. In particular, the ZDT [Deb99] and DTLZ [DTLZ02] test suites can be considered as pioneering work in this area. Both suites follow a so-called top-down approach in which the shape of the Pareto front is defined by a parametric function. In addition, a separate distance function is defined. This function is multiplied with the objective function values of the corresponding Pareto-optimal point. The separation allows the properties of the distance function (multi-modality, density) to be easily adjusted. As a consequence, the decision parameter vector :math:`\mathbf{x}` includes clearly defined location and distance parameters. In addition, the fixed location of the optimum parameters either on the boundary or in the center of the parameter value range was subject to criticism. 

  This strict kind of formulation has been a little loosened over the following years. In particular, more complex Pareto sets have been designed [OJOS04, LZ09]. The basic idea of defining either the properties of the Pareto front or set and then deriving the corresponding problem formulation, however, is still present in established benchmarks proposals [HHBW06, HQD+07]. From experience with problems in engineering, a transfer of this concept to practical problems is questionable. In these problems, it is more likely to have individual objective functions, e. g., lead time, costs and product quality whose joint consideration generates a multi-objective problem [Wag13].

  
.. [Deb99] Kalyanmoy Deb: 
   Multi-objective genetic algorithms: Problem difficulties and construction of test problems.
   Evolutionary Computation, 7 (1999) 3: 205-230
.. [DTLZ02] Kalyanmoy Deb, Lothar Thiele, Marco Laumanns, Eckart Zitzler:
   Scalable multi-objective optimization test problems. 
   CEC 2002: 825–830
.. [OJOS04] T. Okabe, Y. Jin , M. Olhofer, B. Sendhoff:
   On test functions for evolutionary multi-objective optimization.
   PPSN 2004: 792-802
.. [HHBW06] S. Huband, P. Hingston, L. Barone, L. While:
   A review of multiobjective test problems and a scalable test problem toolkit.
   IEEE Transactions on Evolutionary Computation, 10 (2006) 5: 477-506.
.. [HQD+07] V. L. Huang, A. K. Qin, K. Deb, E. Zitzler, P. N. Suganthan, J. J. Liang, M. Preuss, S. Huband:
   Problem definitions for performance assessment of multi-objective optimization algorithms.
   Tech. rep., Nanyang Technological University, Singapore
.. [LZ09] H. Li, Q. Zhang:
   Multiobjective Optimization Problems With Complicated Pareto Sets, MOEA/D and NSGA-II.
   IEEE Transactions on Evolutionary Computation, 13 (2009) 2: 284-302
.. [Wag13] Tobias Wagner:
   Planning and Multi-Objective Optimization of Manufacturing Processes by Means of Empirical Surrogate Models.
   PhD thesis, Technische Universität Dortmund, Germany