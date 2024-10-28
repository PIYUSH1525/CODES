import random
import numpy as np

def calculate_distance(point1, point2):
    return np.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

def route_distance(route, cities):
    distance = 0
    for i in range(len(route)):
        distance += calculate_distance(cities[route[i]], cities[route[(i + 1) % len(route)]])
    return distance


def create_population(population_size, city_count):
    population = []
    for _ in range(population_size):
        route = list(range(city_count))
        random.shuffle(route)
        population.append(route)
    return population

def selection(population, fitness_scores, elite_size):
    selected_population = []
    sorted_pop = [route for _, route in sorted(zip(fitness_scores, population))]
    selected_population.extend(sorted_pop[:elite_size])
    prob = np.array(fitness_scores) / sum(fitness_scores)
    selected_population.extend(random.choices(population, weights=prob, k=len(population) - elite_size))
    return selected_population


def crossover(parent1, parent2):
    start, end = sorted(random.sample(range(len(parent1)), 2))
    child = [-1] * len(parent1)
    child[start:end] = parent1[start:end]
    position = end
    for gene in parent2:
        if gene not in child:
            if position >= len(parent1):
                position = 0
            child[position] = gene
            position += 1
    return child


def mutate(route, mutation_rate=0.01):
    for swapped in range(len(route)):
        if random.random() < mutation_rate:
            swap_with = int(random.random() * len(route))
            route[swapped], route[swap_with] = route[swap_with], route[swapped]
    return route


def genetic_algorithm(cities, population_size=100, elite_size=20, mutation_rate=0.01, generations=500):
    city_count = len(cities)
    population = create_population(population_size, city_count)
    for gen in range(generations):
        fitness_scores = [1 / route_distance(route, cities) for route in population]
        selected_population = selection(population, fitness_scores, elite_size)
        next_generation = []
        for i in range(0, len(selected_population), 2):
            parent1 = selected_population[i]
            parent2 = selected_population[(i + 1) % len(selected_population)]
            child = crossover(parent1, parent2)
            next_generation.append(mutate(child, mutation_rate))
        population = next_generation

    best_route = min(population, key=lambda route: route_distance(route, cities))
    return best_route, route_distance(best_route, cities)


if __name__ == "__main__":
    cities = [(random.randint(0, 100), random.randint(0, 100)) for _ in range(20)]
    best_route, best_distance = genetic_algorithm(cities)
    print("Best Route:", best_route)
    print("Best Distance:", best_distance)
