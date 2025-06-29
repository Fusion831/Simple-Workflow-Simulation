import numpy as np
from collections import deque
from components.Server import Server
from components.task import Task

class Simulation:
    """
    Encapsulates the entire discrete-time workflow simulation.

    This class holds the state of the simulation (servers, queue), manages
    the main event loop, collects data, and calculates summary statistics.
    """

    def __init__(self, num_servers, arrival_lambda, avg_service_time):
        """
        Initializes the simulation environment.

        Args:
            num_servers (int): The number of parallel servers in the system.
            arrival_lambda (float): The average number of tasks arriving per tick (for Poisson dist).
            avg_service_time (float): The average time it takes to process one task (for Exponential dist).
        """
        # Store parameters
        self.num_servers = num_servers
        self.arrival_lambda = arrival_lambda
        self.avg_service_time = avg_service_time

        # Initialize state
        self.server_pool = [Server() for _ in range(self.num_servers)]
        self.task_queue = deque()
        self.current_tick = 0

        # Initialize history/metrics storage in a clean dictionary
        self.history = {
            'queue_length': [],
            'busy_servers': [],
            'wait_times': []
        }

    def _handle_arrivals(self):
        """Handles the arrival of new tasks for the current tick."""
        num_arrivals = np.random.poisson(lam=self.arrival_lambda)
        for _ in range(num_arrivals):
            new_task = Task(tick=self.current_tick, avg_service_time=self.avg_service_time)
            self.task_queue.append(new_task)

    def _tick_servers(self):
        """Ticks each server in the pool to advance their processing time."""
        for server in self.server_pool:
            server.tick()

    def _assign_tasks_to_servers(self):
        """Assigns tasks from the queue to any available idle servers."""
        for server in self.server_pool:
            if not server.is_busy() and self.task_queue:
                next_task = self.task_queue.popleft()
                
                # Calculate and store wait time
                wait_time = self.current_tick - next_task.creation_time
                self.history['wait_times'].append(wait_time)
                
                server.start_new_task(next_task)

    def _collect_metrics(self):
        """Collects and stores the system's state for the current tick."""
        self.history['queue_length'].append(len(self.task_queue))
        busy_server_count = sum(1 for server in self.server_pool if server.is_busy())
        self.history['busy_servers'].append(busy_server_count)

    def get_summary_stats(self):
        """Calculates and returns key performance indicators after the simulation."""
        if not self.history['wait_times']:
             avg_wait_time = 0 # Avoid division by zero
        else:
             avg_wait_time = np.mean(self.history['wait_times'])
        
        total_busy_ticks = sum(self.history['busy_servers'])
        total_available_ticks = self.num_servers * self.current_tick
        
        # Avoid division by zero if simulation duration is 0
        pool_utilization = total_busy_ticks / total_available_ticks if total_available_ticks > 0 else 0

        return {
            "Number of Tasks Completed": len(self.history['wait_times']),
            "Average Wait Time (ticks)": avg_wait_time,
            "Overall Server Pool Utilization": pool_utilization
        }

    def run(self, duration):
        """Runs the simulation for a given number of time ticks."""
        print("--- Starting Simulation ---")
        for tick in range(duration):
            self.current_tick = tick
            self._handle_arrivals()
            self._tick_servers()
            self._assign_tasks_to_servers()
            self._collect_metrics()
        print("--- Simulation Finished ---")