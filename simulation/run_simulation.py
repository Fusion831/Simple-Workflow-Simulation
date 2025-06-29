from simulation.main_simulation import Simulation
import matplotlib.pyplot as plt
import numpy as np


SIMULATION_DURATION = 2000
NUM_SERVERS = 2
ARRIVAL_LAMBDA = 0.8
AVG_SERVICE_TIME = 2.0


# Service rate (mu) is the inverse of average service time
service_rate_mu = 1 / AVG_SERVICE_TIME
# Traffic intensity for a multi-server system is lamda / (N * mu)
rho = ARRIVAL_LAMBDA / (NUM_SERVERS * service_rate_mu)

print(f"--- System Parameters ---")
print(f"Traffic Intensity (rho): {rho:.3f}")
if rho >= 1:
    print("Prediction: System is UNSTABLE. The queue is expected to grow indefinitely.")
else:
    print("Prediction: System is STABLE. The queue should remain bounded.")
print("-" * 25)

# --- 3. CREATE AND RUN THE SIMULATION INSTANCE ---
sim = Simulation(
    num_servers=NUM_SERVERS,
    arrival_lambda=ARRIVAL_LAMBDA,
    avg_service_time=AVG_SERVICE_TIME
)
sim.run(duration=SIMULATION_DURATION)


summary = sim.get_summary_stats()
print("\n--- Simulation Summary ---")
for key, value in summary.items():
    # Format percentages nicely
    if "Utilization" in key:
        print(f"{key}: {value:.2%}")
    else:
        print(f"{key}: {value:.2f}")
print("-" * 25)


history = sim.history
time_axis = np.arange(SIMULATION_DURATION)

plt.figure(figsize=(14, 8))

# Plot 1: Queue Length
plt.subplot(2, 1, 1)
plt.plot(time_axis, history['queue_length'], label='Queue Length', color='blue')
plt.xlabel('Time (ticks)')
plt.ylabel('Number of Tasks in Queue')
plt.title('Queue Length Over Time')
plt.grid(True)
plt.legend()

# Plot 2: Server Busy Status
plt.subplot(2, 1, 2)
plt.plot(time_axis, history['busy_servers'], label='Busy Servers', color='red', drawstyle='steps-post')
plt.xlabel('Time (ticks)')
plt.ylabel('Number of Busy Servers')
plt.title('Server Pool Status Over Time')
plt.yticks(range(NUM_SERVERS + 1))  # Set y-ticks to be integers (0, 1, 2, etc.)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()