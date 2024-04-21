import numpy as np
import tsplib95
from tsplib95.distances import pseudo_euclidean

# Class representing the environment of the ant colony
"""
    rho: pheromone evaporation rate
"""
class Environment:
    def __init__(self, tsp, rho):
        self.rho = rho
        self.problem = tsplib95.load_problem(tsp)
        self.nodes = list(self.problem.get_nodes())
        self.initial_pheromone = 0.5
        self.pheromones = np.full((len(self.nodes), len(self.nodes)), self.initial_pheromone)

        distance_rows = []
        for i in self.nodes:
            distance_row = []
            for j in self.nodes:
                distance = self.calculate_distance(i, j)
                distance_row.append(distance)
            distance_rows.append(distance_row)
        self.distances = np.array(distance_rows)


    def calculate_distance(self, i, j):
        start_coord = self.problem.node_coords[i]
        end_coord = self.problem.node_coords[j]
        distance = pseudo_euclidean(start_coord, end_coord)
        return distance

    # Intialize the pheromone trails in the environment
    def initialize_pheromone_map(self):
        self.pheromones = np.ones((len(self.nodes), len(self.nodes))) / len(self.nodes)

    # Update the pheromone trails in the environment
    def update_pheromone_map(self, ants):
        #evaporate
        self.pheromones *= (1 - self.rho)
        #new pheromone
        for ant in ants:
            for i in range(len(ant.path)-1):
                start_node = ant.path[i]-1
                end_node = ant.path[i+1]-1
                distance_betw_nodes = self.distances[start_node][end_node]
                pheromone_to_add = 1 / distance_betw_nodes
                self.pheromones[start_node][end_node] += pheromone_to_add

    # Get the pheromone trails in the environment
    def get_pheromone(self, i, j):
        adj_i = i-1
        adj_j = j-1
        pheromone_trail = self.pheromones[adj_i][adj_j]
        return pheromone_trail

    # Get the environment topology
    def get_distance(self, i, j):
        adj_i = i-1
        adj_j = j-1
        distance = self.distances[adj_i][adj_j]
        return distance