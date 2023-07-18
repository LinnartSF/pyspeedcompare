"""

this module supports Python code execution time testing, and allows the run time comparison of two functions.
requires time, numpy, and matplotlib.pyplot

"""

__author__ = "Linnart Felkl"
__email__ = "linnartsf@gmail.com"

import time
from matplotlib import pyplot as plt
import numpy as np

class Profiler:
    """ class for comparing runtime performance of two alternative functions

    provides tools for comparing two alternative funtions,
    aiding execution, quantification, and visualization of comparison results

    attrs:
        f1            : first function, must not take args or return values
        f2            : second function for comparison, must also not take args or return values
        size          : amount of comparison reptitions 
        ls_durations1 : execution time for each f1 execution
        ls_durations2 : execution time for each f2 execution
    
    """

    Size :int
    ls_durations1 :list
    ls_durations2 :list
    
    def __init__(self,
                f1,
                f2,
                testsize :int
                ):
        """ constructor """

        self.f1 = f1
        self.f2 = f2
        self.Size = testsize
        self.ls_durations1 = np.zeros(testsize)
        self.ls_durations2 = np.zeros(testsize)
    
    def run(self) -> None:
        """ runs the comparison tests

        runs both functions and measures time used per test run;
        run duration is stored in ls_duration lists, for f1 and f2 respectively

        args:
            None
        
        returns:
            None
        
        sets:
            ls_durations1 (list of float) : stores execution durations of f1 into list
            ls_durations2 (list of float) : stores execution durations of f2 into list
        
        """

        for t in range(self.Size):

            t1 = time.time()

            self.f1()

            t2 = time.time()

            self.ls_durations1[t] = t2 - t1

            t1 = time.time()

            self.f2()

            t2 = time.time()

            self.ls_durations2[t] = t2 - t1
    
    def report(self) -> None:
        """ visualizes comparison results

        plots a histogram showing the distribution in execution times for f1 and f2

        args:
            None
        
        returns:
            None

        sets:
            None
        
        """

        plt.hist(self.ls_durations1, bins = 50, label = "f1", alpha = 0.3)
        plt.hist(self.ls_durations2, bins = 50, label = "f2", alpha = 0.3)
        plt.legend()
        plt.show()

class Simpleprofiler:
    """ class for modeling simple profiler tool
    
    helper class that record start and end time of a time recording;
    when calling stop() method, measured time span is printed into console
    
    attrs:
        t_start (float) : start time of measurement
        t_end   (float) : end time of measurement
    
    methods:
        start ()    -> None : start measurement, and sets t_start
        end   (str) -> None : sets t_end, ending measurement, and printing total time measured
    
    """
    
    t_start :float
    t_end   :float
    
    def __init__(self):
        """ constructor """
        
        self.t_start = 0.0
        self.t_end = 0.0
    
    def start(self, 
              testname :str = ""
              ) -> None:
        """ sets start time of measurement
        
        sets t_start and thereby start time measurement for profiling;
        outputs an optional start message  into console
        
        args:
            testname (str = "") : start message that will be printed into console (optional)
        
        returns:
            None
        
        sets:
            t_start (float) : start time of measurement for profiling
            
        """
        
        print(" -------------------- ")
        
        if testname != "":
            
            print(testname)
        
        self.t_start = time.time()
    
    def stop(self) -> None:
        """ sets end time of measurement and outputs measured time duration
        
        sets t_end and thereby ends time measurement for profiling;
        outputs time measured into console
        
        args:
            None
            
        returns:
            None
        
        sets:
            t_end (float) : end time of measurement for profiling
            
        """
        
        self.t_end = time.time()
        
        print(self.t_end-self.t_start)