import pygame as pg
import sys
from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
import math

light_grey = (200, 200, 200)

key_image = pg.transform.scale_by(pg.image.load('resources/textures/key/1.png'), 2.3)
coin_image = pg.transform.scale_by(pg.image.load('resources/textures/coin/0.png'), 0.3)

class Game:
    def __init__(self):
        pg.init()
        pg.mouse.set_visible(False)
        self.screen = pg.display.set_mode((WIDTH, HEIGHT + 80))
        pg.event.set_grab(True)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        self.coins = []
        self.num_coins = 0
        self.key = True
        self.game_font = pg.font.Font('resources/Cascadia.ttf', 64)
        pg.time.set_timer(self.global_event, 40)
        self.new_game()

    def new_game(self):
        self.player = Player(self)
        self.map = Map(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.key_sprite = AnimatedSprite(self, path='resources/textures/key/1.png', pos=(0, 0), scale=0.3)

        pg.mixer.init()
        self.theme = pg.mixer.music.load('resources/sound/theme.mp3')
        self.coin_sound = pg.mixer.Sound('resources/sound/coin-sound.mp3')
        self.key_sound = pg.mixer.Sound('resources/sound/key.wav')
        pg.mixer.music.set_volume(0.3)
        pg.mixer.music.play(-1)

    def update(self):
        self.player.update()
        self.raycasting.update()
        for coin in self.coins:
            coin.update()
            if math.dist((coin.x, coin.y), self.player.pos()) < 0.5:
                self.coins.remove(coin)
                self.num_coins += 1
                pg.mixer.Sound.play(self.coin_sound)
        if not self.key:
            self.key_sprite.update()
            if math.dist((self.key_sprite.x, self.key_sprite.y), self.player.pos()) < 0.5:
                self.key = True
                pg.mixer.Sound.play(self.key_sound)
        pg.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self):
        # self.screen.fill('black')

        self.object_renderer.draw()

        self.screen.blit(coin_image, (50, HEIGHT + 15))

        coin_text = self.game_font.render(f" :{self.num_coins}", False, light_grey)
        self.screen.blit(coin_text, (60, HEIGHT))

        if self.key:
            self.screen.blit(key_image, (WIDTH - 100, HEIGHT))

        keys = pg.key.get_pressed()
        if keys[pg.K_m]:
            self.map.draw()
            self.player.draw()
            for coin in self.coins:
                pg.draw.circle(self.screen, 'yellow', (coin.x * 100, coin.y * 100), 15)
            if not self.key:
                pg.draw.circle(self.screen, 'blue', (self.key_sprite.x * 100, self.key_sprite.y * 100), 15)
        if keys[pg.K_f]:
            pg.display.toggle_fullscreen()

    def check_events(self):
        self.global_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
