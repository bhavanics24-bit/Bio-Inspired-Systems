import random

target_moisture = 60


def fitness(irrigation):
    moisture = 30 + irrigation

    return abs(target_moisture - moisture)

n = 5

particles = [random.randint(0, 50) for _ in range(n)]

pbest = particles.copy()

gbest = min(pbest, key=fitness)

print("Initial irrigation values:", particles)

for iteration in range(10):

    for i in range(n):

        velocity = random.uniform(-2, 2) + (gbest - particles[i]) * 0.5

        particles[i] = particles[i] + velocity

        particles[i] = max(0, min(50, particles[i]))

        if fitness(particles[i]) < fitness(pbest[i]):
            pbest[i] = particles[i]

    gbest = min(pbest, key=fitness)

print("Optimal irrigation amount:", round(gbest, 2))
print("Final soil moisture:", round(30 + gbest, 2))
print("Fitness value:", round(fitness(gbest), 2))
