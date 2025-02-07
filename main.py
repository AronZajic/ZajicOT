import pygame
from os.path import join
from os import walk

import sys

WINDOW_WIDTH = 960
WINDOW_HEIGHT = 720

class Button:
    def __init__(self, x, y, width, height, foreground_color, background_color, content, fontsize):
        self.font = pygame.font.Font('Cascadia.ttf', fontsize) # load font
        self.image = pygame.Surface((width, height))
        self.image.fill(background_color) # fill the button surface with the background color
        self.rect = self.image.get_frect(topleft=(x, y))
        self.text = self.font.render(content, True, foreground_color) # render the text with the specified foreground color
        self.text_rect = self.text.get_frect(center=(width/2, height/2)) # position the text in the center of the button
        self.image.blit(self.text, self.text_rect) # draw the text onto the button surface

    def is_pressed(self, position, pressed):
        # check if the button is pressed based on the mouse position and the state of the mouse buttons
        if self.rect.collidepoint(position): # check if the mouse is within the bounds of the button
            if pressed[0]: # if the left mouse button is pressed
                return True # button is pressed
            return False # button is not pressed
        return False # mouse is not over the button, so it's not pressed

class Game:
    def __init__(self):
        pygame.init() # initialize Pygame
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("OT Game")
        self.clock = pygame.time.Clock() # create a clock object for controlling frame rate
        self.running = True

    def start_screen(self):
        # display start screen with a start button
        start = True
        start_button = Button(WINDOW_WIDTH//2-50, WINDOW_HEIGHT//2-20, 100, 50, pygame.Color('black'), pygame.Color('white'), 'Start', 32)
        while start:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    start = False
                    self.running = False # quit the game if the window is closed
            mouse_position = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            if start_button.is_pressed(mouse_position, mouse_pressed): # check if start button is pressed
                start = False
                self.run() # start the game
            self.display_surface.blit(start_button.image, start_button.rect)
            self.clock.tick(60)
            pygame.display.update()
    
    def run(self):
        # main game loop
        while self.running:
            delta = self.clock.tick() / 1000 # calculate time difference for frame rate independence

            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.update()  # update the display surface
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.start_screen()