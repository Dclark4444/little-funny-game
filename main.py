import pygame
from pygame_starter import Game
import json, random
from general_functions import *
from map_generation import *

# constants
with open("data.json") as FILE:
    SPRITE_DATA = json.load(FILE)["sprite_data"]

for biome in SPRITE_DATA["biome_sprites"].keys():
    assert biome in SPRITE_DATA["biomes"]


class funny_game(Game):
    def __init__(self):
        super().__init__()
        self.clock = pygame.time.Clock()
        pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.SPRITES = {"blank": pygame.image.load("sprites/blank_hex.png")}
        for biome in SPRITE_DATA["biome_sprites"]:
            if type(SPRITE_DATA["biome_sprites"][biome]) == str:
                self.SPRITES[biome] = pygame.image.load("sprites/" + SPRITE_DATA["biome_sprites"][biome])
            else:
                self.SPRITES[biome] = []
                for index in range(len(SPRITE_DATA["biome_sprites"][biome])):
                    self.SPRITES[biome].append(
                        pygame.image.load("sprites/" + SPRITE_DATA["biome_sprites"][biome][index]))

        self.tile_width = self.SPRITES["blank"].get_size()[0]
        self.tile_height = self.SPRITES["blank"].get_size()[1]
        self.offset_width = (self.SPRITES["blank"].get_size()[0] / 2)
        self.offset_height = (self.SPRITES["blank"].get_size()[1] / 2)

        self.game_map = map()

    def place_tile(self, x, y, img):
        self.screen.blit(img, (x + self.offset_width, y + self.offset_height))

    def display_map_tiles(self, new_map_tiles):
        for row_index, tile_row in enumerate(new_map_tiles):
            hex_offset = 0
            if row_index % 2 == 0:
                hex_offset = self.tile_width / 2
            for col_index, tile in enumerate(tile_row):
                self.place_tile(
                                (col_index * self.tile_width) + hex_offset,
                                (row_index * self.tile_height * 0.75),
                                self.SPRITES[tile.b_type])

    def game(self):
        self.screen.fill((128, 255, 255))
        self.display_map_tiles(self.game_map.tiles)

        running = True
        while running:
            self.clock.tick(60)
            pressed_keys = pygame.key.get_pressed()

            if pressed_keys[pygame.K_q] == pygame.KEYDOWN:
                running = False

        pygame.quit()
        exit()


if __name__ == "__main__":
    instance = funny_game()
    instance.run()
