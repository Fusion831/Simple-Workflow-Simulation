from components.Server import Server
from components.task import Task
from collections import deque
import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
Simulation_Duration = 2000
Arrival_Rate = 0.4


# Initialize the server and the task queue.
my_server = Server()
task_queue = deque()


# Initialize history lists to store the state of the simulation at each tick, helping to visualize the simulation's progress.
queue_length_history = []
server_busy_history = []

#Simulation loop
for tick in range(Simulation_Duration):
    #We check to see if a new task arrives at the server.
    if np.random.rand() < Arrival_Rate:
        new_task = Task(tick)
        task_queue.append(new_task)
    
    my_server.tick()  # Update the server's state for the current tick    
    #If the server is not busy and there are tasks in the queue, we start processing the next task.
    if not my_server.is_busy() and task_queue:
        next_task = task_queue.popleft()
        my_server.start_new_task(next_task)
    # Record the state of the simulation at this tick.
    queue_length_history.append(len(task_queue))
    server_busy_history.append(my_server.is_busy())

#We can now analyze the results of the simulation.


        