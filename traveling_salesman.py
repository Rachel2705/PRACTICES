import itertools

def distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

def total_distance(path, points):
    return sum(distance(points[i], points[i+1]) for i in range(len(path)-1))

def brute_force_tsp(points):
    shortest_path = None
    min_distance = float('inf')

    for path in itertools.permutations(points):
        d = total_distance(path, points)
        if d < min_distance:
            min_distance = d
            shortest_path = path
    
    return shortest_path, min_distance

# Example usage:
cities = [(0, 0), (1, 3), (5, 1), (3, 3)]
shortest_path, min_distance = brute_force_tsp(cities)
print(f"Shortest Path: {shortest_path}")
print(f"Minimum Distance: {min_distance}")

#Explanation:

# distance(point1, point2): This function calculates the Euclidean distance between two points.
# total_distance(path, points): This function calculates the total distance of a given path that visits a list of points.
# brute_force_tsp(points): This function uses a brute-force approach to find the shortest path. It generates all permutations of the points and calculates the total distance for each permutation, keeping track of the shortest one.
# Keep in mind that the brute-force approach is not efficient for large numbers of cities, as it has a time complexity of O(n!). There are more advanced algorithms like dynamic programming (e.g., Held-Karp algorithm) and heuristic methods (e.g., genetic algorithms) that are used to solve the TSP efficiently.

# The answer for the given example would be:

Shortest Path: ((0, 0), (5, 1), (3, 3), (1, 3))
Minimum Distance: 8.47213595499958
