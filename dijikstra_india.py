import csv
import heapq
from collections import defaultdict

# -----------------------------
# STEP 1: LOAD GRAPH FROM CSV
# -----------------------------
def load_graph(filename):
    graph = defaultdict(dict)
    
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            src = row['source']
            dest = row['destination']
            dist = float(row['distance'])
            
            # Undirected graph (roads go both ways)
            graph[src][dest] = dist
            graph[dest][src] = dist
    
    return graph


# -----------------------------
# STEP 2: DIJKSTRA ALGORITHM
# -----------------------------
def dijkstra(graph, start):
    priority_queue = [(0, start)]
    
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    parent = {node: None for node in graph}
    
    while priority_queue:
        current_cost, current_node = heapq.heappop(priority_queue)
        
        if current_cost > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node].items():
            new_cost = current_cost + weight
            
            if new_cost < distances[neighbor]:
                distances[neighbor] = new_cost
                parent[neighbor] = current_node
                heapq.heappush(priority_queue, (new_cost, neighbor))
    
    return distances, parent


# -----------------------------
# STEP 3: RECONSTRUCT PATH
# -----------------------------
def get_path(parent, destination):
    path = []
    
    while destination:
        path.append(destination)
        destination = parent[destination]
    
    return path[::-1]


# -----------------------------
# STEP 4: MAIN FUNCTION
# -----------------------------
def main():
    filename = "india_cities_distances.csv"
    
    graph = load_graph(filename)
    
    print("\nAvailable Cities:")
    for city in graph:
        print(city)
    
    start_city = input("\nEnter source city: ")
    
    if start_city not in graph:
        print("City not found in dataset!")
        return
    
    distances, parent = dijkstra(graph, start_city)
    
    print("\nShortest distances from", start_city)
    print("----------------------------------")
    
    for city in distances:
        print(f"{city}: {distances[city]} km")
    
    print("\nPaths:")
    print("----------------------------------")
    
    for city in graph:
        path = get_path(parent, city)
        print(f"{start_city} -> {city}: {' -> '.join(path)}")


# -----------------------------
# RUN PROGRAM
# -----------------------------
if __name__ == "__main__":
    main()
