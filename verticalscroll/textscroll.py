import pygame

import os

import string

from verticalscroll.config import Config

class TextScroll:
    def __init__(self, window_size):
        self.__split_image()

        self.__text_array = list(Config.scroll_text.lower())
        self.__text_position = []

        for i in range(len(self.__text_array)):
            self.__text_position.append(pygame.math.Vector2(window_size[0] + self.__sprite_width * (i + 1), window_size[1]/2 - self.__sprite_height/2))

    def handle_input(self, pressed, key):
        pass

    def update(self, delta, window_size):
        move = pygame.math.Vector2(Config.animation_speed * -1, 0.0)

        for i in range(len(self.__text_array)):
            self.__text_position[i] += move * delta

        # Restart again to avoid black screen
        if self.__text_position[len(self.__text_array) - 1].x < 0:
            for i in range(len(self.__text_array)):
                self.__text_position[i] = pygame.math.Vector2(window_size[0] + self.__sprite_width * (i + 1), window_size[1]/2 - self.__sprite_height/2)

    def render(self, dest, window_size):
        for i in range(len(self.__text_array)):
            if (self.__text_position[i].x < window_size[0] and self.__text_position[i].x > 0 - self.__sprite_width):
                dest.blit(self.__sprites[self.__text_array[i]], self.__text_position[i].xy)

    def release(self):
        pass

    def __split_image(self):
        image = pygame.image.load(os.path.join(*Config.font_sprites_filename)).convert_alpha()

        self.__sprite_width = image.get_width()/10
        self.__sprite_height = image.get_height()/6
        self.__sprites = {}

        self.__sprites[" "] = image.subsurface(0, 0, self.__sprite_width, self.__sprite_height)
        self.__sprites[","] = image.subsurface(2 * self.__sprite_width, self.__sprite_height, self.__sprite_width, self.__sprite_height)
        self.__sprites["."] = image.subsurface(4 * self.__sprite_width, self.__sprite_height, self.__sprite_width, self.__sprite_height)

        sprite_index = 0
        for i in range(6, 16):
            self.__sprites[str(sprite_index)] = image.subsurface((i % 10) * self.__sprite_width, (i // 10 + 1) * self.__sprite_height, self.__sprite_width, self.__sprite_height)
            sprite_index += 1

        sprite_index = 97
        for i in range(3, 29):
            self.__sprites[chr(sprite_index)] = image.subsurface((i % 10) * self.__sprite_width, (i // 10 + 3) * self.__sprite_height, self.__sprite_width, self.__sprite_height)
            sprite_index += 1

        # Relocate correctly 'v' and 'w' chars
        self.__sprites['temp'] = self.__sprites['w']
        self.__sprites['w'] = self.__sprites['v']
        self.__sprites['v'] = self.__sprites.pop('temp', None)