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
        self.SPRITES = {"blank": "sprites/blank_hex.png"}
        for biome in SPRITE_DATA["biome_sprites"]:
            if type(SPRITE_DATA["biome_sprites"][biome]) == str:
                self.SPRITES[biome] = pygame.image.load("sprites/" + SPRITE_DATA["biome_sprites"][biome])
            else:
                self.SPRITES[biome] = []
                for file_path in SPRITE_DATA["biome_sprites"][biome]:
                    self.SPRITES[biome].append(
                        pygame.image.load("sprites/" + SPRITE_DATA["biome_sprites"][biome][file_path]))

    def game(self):
        self.screen.fill((128, 255, 255))

        self.screen.blit(
            self.SPRITES["blank"],
            (
                self.screen_size[0] / 2 - self.SPRITES["blank"].get_size()[0],
                self.screen_size[1] / 2 - self.SPRITES["blank"].get_size()[1],
            ),
        )

if __name__ == "__main__":
    instance = funny_game()
    instance.run()




