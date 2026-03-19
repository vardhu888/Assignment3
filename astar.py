import heapq
import random

# Grid size
GRID_SIZE = 70

# Directions (4-direction movement)
DIRECTIONS = [(-1,0),(1,0),(0,-1),(0,1)]

# -----------------------------
# Generate Grid with Obstacles
# -----------------------------
def generate_grid(density_level):
    grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    
    # Density levels
    if density_level == "low":
        prob = 0.1
    elif density_level == "medium":
        prob = 0.25
    else:
        prob = 0.4
    
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if random.random() < prob:
                grid[i][j] = 1   # obstacle
    
    return grid


# -----------------------------
# Heuristic (Manhattan distance)
# -----------------------------
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# -----------------------------
# A* Algorithm
# -----------------------------
def a_star(grid, start, goal):
    pq = [(0, start)]
    
    g_cost = {start: 0}
    parent = {start: None}
    
    visited = set()
    
    while pq:
        _, current = heapq.heappop(pq)
        
        if current == goal:
            break
        
        if current in visited:
            continue
        
        visited.add(current)
        
        for d in DIRECTIONS:
            nx, ny = current[0] + d[0], current[1] + d[1]
            
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                if grid[nx][ny] == 1:
                    continue
                
                neighbor = (nx, ny)
                new_cost = g_cost[current] + 1
                
                if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                    g_cost[neighbor] = new_cost
                    f_cost = new_cost + heuristic(neighbor, goal)
                    heapq.heappush(pq, (f_cost, neighbor))
                    parent[neighbor] = current
    
    return parent, g_cost


# -----------------------------
# Reconstruct Path
# -----------------------------
def get_path(parent, start, goal):
    if goal not in parent:
        return None
    
    path = []
    node = goal
    
    while node:
        path.append(node)
        node = parent[node]
    
    return path[::-1]


# -----------------------------
# Measures of Effectiveness
# -----------------------------
def evaluate(path, explored_nodes):
    if path is None:
        return {
            "Path Found": False,
            "Path Length": None,
            "Nodes Explored": explored_nodes
        }
    
    return {
        "Path Found": True,
        "Path Length": len(path),
        "Nodes Explored": explored_nodes
    }


# -----------------------------
# MAIN PROGRAM
# -----------------------------
def main():
    density = input("Enter obstacle density (low/medium/high): ")
    
    grid = generate_grid(density)
    
    start = (0, 0)
    goal = (69, 69)
    
    # Ensure start & goal are free
    grid[start[0]][start[1]] = 0
    grid[goal[0]][goal[1]] = 0
    
    parent, g_cost = a_star(grid, start, goal)
    
    path = get_path(parent, start, goal)
    
    result = evaluate(path, len(g_cost))
    
    print("\n--- Results ---")
    print("Path Found:", result["Path Found"])
    print("Path Length:", result["Path Length"])
    print("Nodes Explored:", result["Nodes Explored"])
    
    if path:
        print("\nPath:")
        print(path)


if __name__ == "__main__":
    main()
