import numpy as np
class Server:
    """Represents a server that processes tasks in the workflow simulation.
    It will handle the processing of tasks with the time, and will contain Helper methods:
    - is_busy(): Check if the server is currently processing a task.
    - start_new_task(task): Sets current task and starts processing it.
                         sets the time remaing to processing time.
    - tick(): calls busy() to check if the server is busy, and if so, decrements the processing time.
             When time reaches zero, the task is completed and the server is no longer busy. 
    """
    def __init__(self, avg_service_time: float = 3.0):
        """Initialize the task with an exponentially distributed processing time
           and the tick when it was created."""
        self.current_task = None
        # np.random.exponential returns a float. We must round it to an integer
        # and ensure it's at least 1, since a task can't take 0 ticks.
        self.processing_time = max(1, round(np.random.exponential(scale=avg_service_time)))
        
    def is_busy(self) -> bool:
        """Check if the server is currently processing a task."""
        if self.current_task is None:
            return False
        return True
    def start_new_task(self, task):
        """Sets the current task and starts processing it.
        sets the processing time to the task's processing time."""
        self.current_task = task
        self.processing_time = task.processing_time
    
    def tick(self):
        """Decrements the processing time if the server is busy.
        When processing time reaches zero, the task is completed and the server is no longer busy."""
        if self.is_busy():
            self.processing_time -= 1
            if self.processing_time <= 0:
                self.current_task = None
                self.processing_time = 0