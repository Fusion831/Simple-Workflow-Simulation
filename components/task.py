import numpy as np

class Task:
    """
    Represents a single unit of work in the simulation.

    Each task has a unique creation time and a processing time that
    determines how long a server must work on it.
    """
    
    def __init__(self, tick: int, avg_service_time: float):
        """
        Initializes a new Task.

        Args:
            tick (int): The simulation time (tick) when the task was created.
                        This is crucial for calculating waiting time.
            avg_service_time (float): The average service time for all tasks, used as
                                      the scale parameter for the exponential distribution.
        """
        # Store the time this task was created.
        self.creation_time = tick
        
        # Generate the processing time for this specific task.
        # It's drawn from an exponential distribution to model realistic service times.
        # We round the result and ensure it's at least 1 tick long.
        self.processing_time = max(1, round(np.random.exponential(scale=avg_service_time)))

    def __repr__(self):
        """Provides a developer-friendly string representation of the Task object."""
        return (f"Task(created_at={self.creation_time}, "
                f"processing_time={self.processing_time})")