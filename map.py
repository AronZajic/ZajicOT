import pygame as pg
from settings import *
from maze import *
from sprite import *
import random

_ = False

simple_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [3, _, _, _, _, _, _, _, _, _, _, _, _, _, 2],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
    [_, _, _, _, _, _, _, _, _, _, _, _, _, _, _],
]

class Map:
    def __init__(self, game):
        self.game = game
        self.simple_map = simple_map
        self.game.key = True
        self.game.coins.append(AnimatedSprite(game, path='resources/textures/coin/0.png', pos=(5.5, 1.5), scale=0.3))
        self.world_map = {}
        self.rows = len(self.simple_map)
        self.cols = len(self.simple_map[0])
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.simple_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        for pos in self.world_map:
            if self.world_map[pos] == 1:
                pg.draw.rect(self.game.screen, 'white', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
            if self.world_map[pos] == 2:
                pg.draw.rect(self.game.screen, 'red', (pos[0] * 100, pos[1] * 100, 100, 100), 2)
            if self.world_map[pos] == 3:
                pg.draw.rect(self.game.screen, 'blue', (pos[0] * 100, pos[1] * 100, 100, 100), 2)


    def new_map(self):
        self.world_map = {}
        self.simple_map = generate_maze(self.cols, self.rows)
        self.game.coins = []

        coin_pos = []

        for i in range(5):
            x = random.randint(1, self.cols - 2)
            y = random.randint(1, self.rows - 2)

            while self.simple_map[y][x] != False or not (1 < x or 1 < y) or (x,y) in coin_pos:
                x = random.randint(1, self.cols - 2)
                y = random.randint(1, self.rows - 2)

            coin_pos.append((x,y))

            self.game.coins.append(AnimatedSprite(self.game, path='resources/textures/coin/0.png', pos=(x + 0.5, y + 0.5), scale=0.3))

        x = random.randint(1, self.cols - 2)
        y = random.randint(1, self.rows - 2)

        while self.simple_map[y][x] != False or not (1 < x or 1 < y) or (x,y) in coin_pos:
            x = random.randint(1, self.cols - 2)
            y = random.randint(1, self.rows - 2)

        self.game.key_sprite = Sprite(self.game, path='resources/textures/key/0.png', pos=(x + 0.5, y + 0.5), scale=0.3)

        self.get_map()