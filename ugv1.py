import heapq
import random

GRID_SIZE = 20
DIRECTIONS = [(-1,0),(1,0),(0,-1),(0,1)]


# -----------------------------
# Generate Grid
# -----------------------------
def generate_grid(prob=0.1):
    grid = [[1 if random.random() < prob else 0 for _ in range(GRID_SIZE)]
            for _ in range(GRID_SIZE)]
    
    # Ensure start and goal are free
    grid[0][0] = 0
    grid[GRID_SIZE-1][GRID_SIZE-1] = 0
    
    return grid


# -----------------------------
# Heuristic (Manhattan)
# -----------------------------
def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


# -----------------------------
# A* Algorithm
# -----------------------------
def a_star(grid, start, goal):
    pq = [(0, start)]
    g_cost = {start: 0}
    parent = {start: None}
    
    while pq:
        _, current = heapq.heappop(pq)
        
        if current == goal:
            break
        
        for dx, dy in DIRECTIONS:
            nx, ny = current[0]+dx, current[1]+dy
            
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                if grid[nx][ny] == 1:
                    continue
                
                new_cost = g_cost[current] + 1
                
                if (nx, ny) not in g_cost or new_cost < g_cost[(nx, ny)]:
                    g_cost[(nx, ny)] = new_cost
                    f = new_cost + heuristic((nx, ny), goal)
                    heapq.heappush(pq, (f, (nx, ny)))
                    parent[(nx, ny)] = current
    
    return parent


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
# Dynamic Obstacles
# -----------------------------
def introduce_dynamic_obstacles(grid, step):
    if step % 5 == 0:
        x = random.randint(0, GRID_SIZE-1)
        y = random.randint(0, GRID_SIZE-1)
        
        if (x, y) != (0, 0) and (x, y) != (GRID_SIZE-1, GRID_SIZE-1):
            grid[x][y] = 1


# -----------------------------
# Dynamic Path Planning
# -----------------------------
def dynamic_path_planning(grid, start, goal):
    current = start
    path_taken = [current]
    
    steps = 0
    replans = 0
    
    while current != goal:
        parent = a_star(grid, current, goal)
        path = get_path(parent, current, goal)
        
        if path is None:
            return None, steps, replans
        
        for next_node in path[1:]:
            steps += 1
            
            # introduce dynamic change
            introduce_dynamic_obstacles(grid, steps)
            
            # obstacle appeared → replan
            if grid[next_node[0]][next_node[1]] == 1:
                print("️Obstacle detected! Replanning...")
                replans += 1
                break
            
            current = next_node
            path_taken.append(current)
            
            if current == goal:
                return path_taken, steps, replans
    
    return path_taken, steps, replans


# -----------------------------
# Print Grid (Optional)
# -----------------------------
def print_grid(grid, path=None):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if (i, j) == (0, 0):
                print("S", end=" ")
            elif (i, j) == (GRID_SIZE-1, GRID_SIZE-1):
                print("G", end=" ")
            elif path and (i, j) in path:
                print("*", end=" ")
            elif grid[i][j] == 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()


# -----------------------------
# MAIN
# -----------------------------
def main():
    start = (0, 0)
    goal = (GRID_SIZE-1, GRID_SIZE-1)
    
    max_attempts = 5
    
    for attempt in range(max_attempts):
        print(f"\nAttempt {attempt+1}")
        
        grid = generate_grid(prob=0.1)
        
        path, steps, replans = dynamic_path_planning(grid, start, goal)
        
        if path:
            print("\n Path Found!")
            print("Path Length:", len(path))
            print("Steps Taken:", steps)
            print("Replans:", replans)
            
            print("\nGrid Visualization:")
            print_grid(grid, path)
            
            return
    
    print("\nNo path found after multiple attempts.")


if __name__ == "__main__":
    main()
