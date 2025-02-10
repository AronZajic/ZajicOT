import random

empty = False
wall = 1
exit = 2
enterance = 3

# Function to generate a maze using Depth-First Search
def generate_maze(width, height):
    maze = [[wall for _ in range(width)] for _ in range(height)]

    def carve_passages(x, y):
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= ny < height and 0 <= nx < width and maze[ny][nx] == wall:
                maze[ny - dy // 2][nx - dx // 2] = empty
                maze[ny][nx] = empty
                carve_passages(nx, ny)

    # Start carving from the top-left corner
    start_x, start_y = 1, 1
    maze[start_y][start_x] = empty
    carve_passages(start_x, start_y)

    # Add an exit at the bottom right corner
    for x in range(width - 2, 0, -1):
        if maze[height - 2][x] == empty:
            maze[height - 1][x] = exit
            break
    
    maze[1][0] = enterance

    # print_maze(maze)
    return maze

# Function to print the maze
def print_maze(maze):
    for row in maze:
        for cell in row:
            if cell == empty:
                print(' ', end='')
            else:
                print(cell, end='')
        print()

# Parameters for the maze size (must be odd for a perfect maze)
# maze_width = 17
# maze_height = 9

# maze = generate_maze(maze_width, maze_height)
# print_maze(maze)
