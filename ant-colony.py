from environment import Environment
from ant import Ant

# Class representing the ant colony
"""
    ant_population: the number of ants in the ant colony
    iterations: the number of iterations 
    alpha: a parameter controlling the influence of the amount of pheromone during ants' path selection process
    beta: a parameter controlling the influence of the distance to the next node during ants' path selection process
    rho: pheromone evaporation rate
"""
class AntColony:
    def __init__(self, tsp, count_ants, rho, alpha, beta):
        self.environment = Environment(tsp, rho)
        self.solution = None
        self.distance = float('inf')
        self.ants = []
        for i in range(count_ants):
            new_ant = Ant(self.environment, alpha, beta)
            self.ants.append(new_ant)

    # Solve the ant colony optimization problem
    def solve(self):
        for ant in self.ants:
            ant.run()
            path_length = 0
            for i in range(len(ant.path) - 1):
                single_length = self.environment.get_distance(ant.path[i], ant.path[i+1])
                path_length += single_length
            if path_length < self.distance:
                self.distance = path_length
                self.solution = ant.path
        self.environment.update_pheromone_map(self.ants)
        return self.solution, self.distance

def main():
    # Intialize the ant colony
    ant_colony = AntColony('./att48-specs/att48.tsp', 48, 0.5, 1, 5)
    # Solve the ant colony optimization problem
    solution, distance = ant_colony.solve()
    print("Solution: ", solution)
    print("Distance: ", distance)

if __name__ == '__main__':
    main()
