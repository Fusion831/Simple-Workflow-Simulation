from components.Server import Server
from components.task import Task
from collections import deque
import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
Simulation_Duration = 2000
Arrival_Rate = 0.4
LAMBDA = 0.4


# Initialize the server and the task queue.
my_server = Server()
task_queue = deque()


# Initialize history lists to store the state of the simulation at each tick, helping to visualize the simulation's progress.
queue_length_history = []
server_busy_history = []
wait_times = []  # This will store the waiting time for each task in the queue.

#Simulation loop
for tick in range(Simulation_Duration):
    #We check to see if a new task arrives at the server.
    num_arrivals = np.random.poisson(LAMBDA)  # Generate a random number of arrivals based on the Poisson distribution.
    for _ in range(num_arrivals):
        new_task = Task(tick)
        task_queue.append(new_task)
    
    my_server.tick()  # Update the server's state for the current tick    
    #If the server is not busy and there are tasks in the queue, we start processing the next task.
    if not my_server.is_busy() and task_queue:
        next_task = task_queue.popleft()
        wait_time = tick - next_task.creation_time
        wait_times.append(wait_time)
        my_server.start_new_task(next_task)
    # Record the state of the simulation at this tick.
    queue_length_history.append(len(task_queue))
    server_busy_history.append(my_server.is_busy())
    


#What is the Exact Server Utilization?
server_utilization = sum(server_busy_history) / len(server_busy_history)
print(f"Server Utilization: {server_utilization:.2f}") #found to be close to 1.

# The server utilization is the proportion of time the server is busy.

if wait_times:  # Check if the list is not empty to avoid division by zero
    average_wait_time = sum(wait_times) / len(wait_times)
    print(f"Number of tasks completed: {len(wait_times)}")
    print(f"Average Wait Time: {average_wait_time:.2f} ticks")
else:
    print("No tasks were completed during the simulation.")


#We can now analyze the results of the simulation.

time = np.arange(Simulation_Duration)
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(time, queue_length_history, label='Queue Length', color='blue')
plt.xlabel('Time (ticks)')
plt.ylabel('Queue Length')
plt.title('Queue Length Over Time')
plt.grid()
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(time, server_busy_history, label='Server Busy', color='red')
plt.xlabel('Time (ticks)')
plt.ylabel('Server Busy (1 = Busy, 0 = Idle)')
plt.title('Server Busy Status Over Time')
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()


        