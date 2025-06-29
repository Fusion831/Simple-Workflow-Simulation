class Task:
    """Represents a task to be handled in the workflow simulation.
    it will instantiate the task with a random time to complete.
    and will also store the tick(t) when the task was created.
    """
    def __init__(self,tick: int):
        """Initialize the task with a random time to complete and the tick when it was created."""
        import random
        self.processing_time = random.randint(1, 5)
        self.creation_time= tick