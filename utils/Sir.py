import random
import networkx as nx
import matplotlib.pyplot as plt
import os


class Sir:

    def __init__(self, graph, infection_rate, recovery_rate, initial_infected, time_infected, position):
        self.graph = graph
        self.infection_rate = infection_rate
        self.recovery_rate = recovery_rate
        self.initial_infected = initial_infected
        self.time_infected = time_infected
        self.position = position

        self.labels = {}
        self.colors = ['blue'] * len(graph.nodes())
        self.time_traker = [0] * len(graph.nodes())

        for node in enumerate(graph.nodes()):
            self.labels[node[1]] = "S"

        self.prepare_directory()

    def initial_infection(self):
        for node in random.sample(list(self.graph.nodes()), self.initial_infected):
            self.labels[node] = "I"
            self.colors[node] = "red"
            self.time_traker[node] += 1

    def model(self):

        print("Running SIR model 🦠")

        # Run the infection
        self.infect()

        # Run the recovery
        self.recover()

    def infect(self):
        # find the infected nodes
        infected_nodes = [node for node in self.graph.nodes()
                          if self.labels[node] == "I"]

        # Find the non infected nieghbors of infected nodes
        non_infected_neighbors = []
        for node in infected_nodes:
            for neighbor in self.graph.neighbors(node):
                if self.labels[neighbor] == "S":
                    non_infected_neighbors.append(neighbor)

        # Infect the non infected neighbors
        for node in non_infected_neighbors:
            if random.random() < self.infection_rate:
                self.labels[node] = "I"
                self.colors[node] = "red"

        for node in self.graph.nodes():
            if (self.colors[node] == "red"):
                self.time_traker[node] += 1

    def recover(self):
        # Recover the infected nodes
        for t in range(len(self.time_traker)):
            if (self.time_traker[t] > self.time_infected):

                # Here is the contagion happening
                if (random.uniform(0, 1) < self.recovery_rate):
                    self.colors[t] = 'green'
                    self.labels[t] = 'R'

    def save_graph(self, name):
        plt.figure(name)

        nx.draw(
            self.graph,
            self.position,
            node_color=self.colors,
            edge_color='#d5d5d5',
            font_color='white',
            node_size=30
        )
        plt.savefig("images/{name}.png".format(name=name), dpi=500)
        plt.close()

    def create_movie(self):
        print("Creating movie 🔨")
        try:
            os.system(
                "ffmpeg -framerate 1 -i images/step_%d.png -c:v libx264 -r 30 -pix_fmt yuv420p movie.mp4 -y >> /dev/null 2>&1 && echo 'Movie created! 🎥 '"
            )
        except:
            print("Error creating movie! 😢")

    def prepare_directory(self):
        if not os.path.exists("images"):
            os.makedirs("images")
        else:
            os.system("rm images/*")

    def print_statistics(self, step):
        print(f"SIR stopped {step -1} steps!")
        recovered = sum(value == "R" for value in self.labels.values())
        number_of_nodes = len(self.graph.nodes())
        intact = number_of_nodes - recovered
        print(f"{recovered}/{number_of_nodes} nodes infected -> recovered!")
        print(f"{intact}/{number_of_nodes} nodes were intact!")
