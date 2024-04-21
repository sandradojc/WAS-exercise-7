import numpy as np

# Class representing an artificial ant of the ant colony
"""
    alpha: a parameter controlling the influence of the amount of pheromone during ants' path selection process
    beta: a parameter controlling the influence of the distance to the next node during ants' path selection process
"""
class Ant:
    def __init__(self, environment, alpha: float, beta: float):
        self.environment = environment
        self.alpha = alpha
        self.beta = beta
        self.path = []
        self.curr_node = np.random.choice(self.environment.nodes)

    # The ant runs to visit all the possible locations of the environment
    def run(self):
        self.path = [self.curr_node]
        while len(set(self.path)) < len(self.environment.nodes):
            self.select_path()
        self.path.append(self.path[0])

    # Select the next path based on the random proportional rule of the ACO algorithm
    def select_path(self):
        unvisited = set(self.environment.nodes) - set(self.path)
        probabilities = []
        for next_node in unvisited:
            pheromone = self.environment.get_pheromone(self.curr_node, next_node) ** self.alpha
            closeness = (1.0 / self.environment.get_distance(self.curr_node, next_node)) ** self.beta
            probabilities.append(pheromone * closeness)
        probabilities = np.array(probabilities) / np.sum(probabilities)
        next_node = np.random.choice(list(unvisited), p=probabilities)
        self.path.append(next_node)
        self.curr_node = next_node

    '''
    # Position an ant in an environment
    def join(self, environment):
        self.environment = environment
    '''