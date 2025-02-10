# Game Design Document - 3D maze game

Autor: Áron Zajíc
Vybratá téma: One level, but constantly changing (jeden level, ale neustále sa mení)

## 1. Úvod

Cieľom hry je nájsť cestu von z bludiska. Hra používa techniku raycasting pre vykreslenie pseudo 3D prostredia pre navigáciu v bludisku.

### 1.1 Inšpirácia

Wolfenstein 3D

<p align="center">
  <img src="https://github.com/AronZajic/ZajicOT/blob/main/screenshot.jpg" alt="Wolfenstein 3D">
  <br>
  <em>Ukážka hry Wolfenstein 3D</em>
</p>


Je to asi najznámejšia hra, ktorá používa raycasting.

### 1.2 Použité technológie

Pygame-CE: knižnica pre vykresľovanie
VS Code: IDE

## 2. Koncept

### 2.1 Priebeh hry

Hráč sa zobudí v bludisku z ktorého musí nájsť cestu von. Prvá úroveň je veľmi jednoduchá, je to iba jedna ulička a dvere skoré sú cestou von z bludiska sú ihneď viditeľné. Po prekročení týchto dverí hráč je transportovaný do novej úrovne, ktorá je už ale ozajstným bludiskom tak nájdenie dverí pre cestu von je ťažšie. Každá ďalšia úroveň je takto generovaná.

### 2.2 Interpretácia témy - One level, but constantly changing

Herné úrovne(bludiská) hry sa náhodne generujú pri čom veľkosť hracej plochy a ciel hry ostáva ten istý.

### 2.3 Návrh tried

** Game: ** Hlavná trieda hry v ktorej sa vytvorí okno hry.

** Player: ** Trieda ktorá reprezentuje hráča napríklad sa tu ukladá jeho pozícia. Trieda je ďalej zodpovedná pre testovanie kolízie zo stenami bludiska a ovládania hráča.

** Map: ** Trieda reprezentujúca mapu bludiska.

** Maze: ** Súbor s pomocnými funkciami pre generovanie náhodného bludiska.

** ObjectRenderer: ** Trieda ktorá je zodpovedná za načítanie textúr pre steny bludiska a vykresľovanie daných stien.

** RayCasting: ** Trieda v ktorej sa robia výpočty pre vykresľovanie pseudo 3D sveta.

** Settings: ** Súbor uchovávajúci globálne nastavenia.

# ChatGPT:

You said:

    Python code for generating a 2D array that is a maze.
    
ChatGPT said:

    Here’s a Python script to generate a 2D array that represents a maze using a simple randomized depth-first search (DFS) algorithm.
    
import random

// Function to generate a maze using Depth-First Search
def generate_maze(width, height):
    maze = [['#' for _ in range(width)] for _ in range(height)]
    
    def carve_passages(x, y):
        directions = [(0, 2), (0, -2), (2, 0), (-2, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= ny < height and 0 <= nx < width and maze[ny][nx] == '#':
                maze[ny - dy // 2][nx - dx // 2] = ' '
                maze[ny][nx] = ' '
                carve_passages(nx, ny)
                
    // Start carving from the top-left corner
    start_x, start_y = 1, 1
    maze[start_y][start_x] = ' '
    carve_passages(start_x, start_y)
    
    return maze
    
// Function to print the maze
def print_maze(maze):
    for row in maze:
        print(''.join(row))
        
// Parameters for the maze size (must be odd for a perfect maze)
maze_width = 21  // Example: 21
columnsmaze_height = 11  // Example: 11 rows

maze = generate_maze(maze_width, maze_height)
print_maze(maze)

How It Works:

The maze is represented as a 2D array of # for walls and spaces ( ) for paths.

It uses a recursive depth-first search (DFS) to carve out paths in the maze.

The algorithm ensures that the maze is fully connected without loops.

Customize:

maze_width and maze_height can be adjusted. They must be odd numbers for a proper maze structure.

You can modify the carve_passages function to create different maze patterns or add an entrance and exit.

Would you like to visualize it as an image instead? I can help with that!


