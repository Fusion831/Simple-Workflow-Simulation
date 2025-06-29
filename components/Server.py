class Server:
    """Represents a server that processes tasks in the workflow simulation.
    It will handle the processing of tasks with the time, and will contain Helper methods:
    - is_busy(): Check if the server is currently processing a task.
    - start_new_task(task): Sets current task and starts processing it.
                         sets the time remaing to processing time.
    - tick(): calls busy() to check if the server is busy, and if so, decrements the processing time.
             When time reaches zero, the task is completed and the server is no longer busy. 
    """
    def __init__(self):
        """Initialize the server to be "idle" at the given tick.
        sets the current task to None, and the processing time to 0."""
        self.current_task = None
        self.processing_time = 0