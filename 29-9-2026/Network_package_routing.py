import random

# Network and packet routes
routes = [
    ["A", "B", "E"],
    ["A", "C", "E"],
    ["A", "B", "C", "E"],
    ["A", "C", "D", "E"]
]

# Cost of each route
cost = [6, 8, 7, 5]

# Genetic Algorithm
for generation in range(5):

    # Select the best 2 routes
    best = sorted(zip(cost, routes))[:2]

    # Crossover
    new_route = best[0][1][:2] + best[1][1][2:]

    # Mutation
    if random.random() < 0.3:
        new_route = random.choice(routes)

    # Add new route
    routes.append(new_route)
    cost.append(random.randint(5, 10))

# Find best route
best_index = cost.index(min(cost))

print("Best Packet Route:", routes[best_index])
print("Minimum Cost:", cost[best_index])
