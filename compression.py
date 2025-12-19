import numpy as np
import cv2
from metrics import mse
import random

class GeneticCompressor:
    def __init__(self, original_image, pop_size=20, generations=50):
        self.original = original_image
        self.pop_size = pop_size
        self.generations = generations
        self.h, self.w, _ = original_image.shape

    def initialize_population(self):
        base = cv2.resize(self.original, (200, 120))
        population = []
        for _ in range(self.pop_size):
            noise = np.random.randint(-20, 20, base.shape)
            individual = np.clip(base + noise, 0, 255).astype(np.uint8)
            population.append(individual)
        return population


    def fitness(self, candidate):
        upscaled = cv2.resize(candidate, (self.w, self.h))
        return -mse(self.original, upscaled)

    def select(self, population, fitnesses):
        idx = np.argsort(fitnesses)[-5:]
        return [population[i] for i in idx]

    def crossover(self, parent1, parent2):
        mask = np.random.rand(*parent1.shape) > 0.5
        child = np.where(mask, parent1, parent2)
        return child.astype(np.uint8)

    def mutate(self, image, rate=0.01):
        mutation_mask = np.random.rand(*image.shape) < rate
        noise = np.random.randint(-20, 20, image.shape)
        image = image + mutation_mask * noise
        return np.clip(image, 0, 255).astype(np.uint8)

    def run(self):
        population = self.initialize_population()

        for gen in range(self.generations):
            fitnesses = [self.fitness(ind) for ind in population]
            best = population[np.argmax(fitnesses)]

            selected = self.select(population, fitnesses)
            new_population = selected.copy()

            while len(new_population) < self.pop_size:
                p1, p2 = random.sample(selected, 2)
                child = self.crossover(p1, p2)
                child = self.mutate(child)
                new_population.append(child)

            population = new_population
            print(f"Generation {gen} completed")

        return best
