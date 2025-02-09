import pygame as pg
from settings import *
from maze import *

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
        self.get_map()