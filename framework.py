import time

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
        """ constructor
        
        class Profiler class constructor
        
        args:
            None
        
        returns:
            None
        
        sets:
            t_start (float) : start time of measurement, set to default
            t_end   (float) : end time of measurement, set to default
        
        """
        
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