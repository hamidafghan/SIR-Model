import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from utils.Graph import graph
from utils.Sir import Sir
from scipy.interpolate import make_interp_spline

graph = nx.convert_node_labels_to_integers(graph)
position = nx.kamada_kawai_layout(graph)

# It is very recommended to change the property and analyze the result. 
infection_rate = 0.2
recovery_rate = 0.3
initial_infected = 1
time_infected = 3
step = 0

susceptible = [len(graph) - initial_infected]
infected = [initial_infected]
recovered = [0]

sir = Sir(
    graph,
    infection_rate,
    recovery_rate,
    initial_infected,
    time_infected,
    position)

sir.save_graph("step_0")
step += 1

sir.initial_infection()

sir.save_graph("step_1")
step += 1


# Loop until all nodes are recovered
while (sir.colors.count('green') + sir.colors.count('blue') < len(sir.colors)):

    # Run the infecton and recovery
    sir.model()

    # Save the graph
    sir.save_graph("step_" + str(step))

    susceptible = susceptible + [sir.colors.count('blue')]
    infected = infected + [sir.colors.count('red')]
    recovered = recovered + [sir.colors.count('green')]

    step += 1

# Print the statistics
sir.print_statistics(step=step)

sir.create_movie()


# Dataset
x = np.array(range(0, len(susceptible)))
y = np.array(susceptible)
y1 = np.array(infected)
y2 = np.array(recovered)

X_Y_Spline = make_interp_spline(x, y)
X_Y1_Spline = make_interp_spline(x, y1)
X_Y2_Spline = make_interp_spline(x, y2)

time = np.linspace(x.min(), x.max(), 500)
susceptible = X_Y_Spline(time)
infected = X_Y1_Spline(time)
recovered = X_Y2_Spline(time)

# Plotting the Graph
plt.plot(time, susceptible)
plt.plot(time, infected)
plt.plot(time, recovered)
plt.legend(['Susceptible', 'Infected', 'Recovered'])
plt.title("Sir Model")
plt.xlabel("Time (days)")
plt.ylabel("Number of people")
plt.show()
