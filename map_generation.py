import json, random
from general_functions import *

# constants
with open("data.json") as FILE:
    MAP_DATA = json.load(FILE)["map_data"]

class biome:
    def __init__(self, b_type, richness, has_river = False):
        self.b_type = b_type
        self.richness = richness
        self.has_river = has_river

class map:
    def __init__(self):
        self.height = MAP_DATA["height"]
        self.width = MAP_DATA["width"]
        self.tiles = self.get_tile_shape()
        self.generate_map()

    def get_tile_shape(self):
        if MAP_DATA["abstract_shape"] == 0:
            return [[biome("desert", 0) for _ in range(self.width)] for _ in range(self.height)]
        else:
            shape = [[biome("water", 0) for _ in range(self.width)] for _ in range(self.height)]

            for x in range(self.height):
                for y in range(self.width):

                    land_frequency = MAP_DATA["land_frequency"]

                    for x_mod in range(-1, 2):
                        for y_mod in range(-1, 2):

                            x_with_mod = x + x_mod
                            y_with_mod = y + y_mod

                            if x_with_mod < 0 or x_with_mod >= self.width or y_with_mod < 0 or y_with_mod >= self.height:
                                land_frequency -= MAP_DATA["contiguous_water"] / 9
                            elif shape[x_with_mod][y_with_mod].b_type == "water":
                                land_frequency -= MAP_DATA["contiguous_water"] / 9
                            else:
                                pass
                            land_frequency -= MAP_DATA["island_frequency"] / 9

                    if land_frequency >= random.random():
                        shape[x][y] = biome("desert", 0)

            return shape


    def pick_compare_biomes(self, biome_modifiers):
        biome_totals = {}
        for biome in biome_modifiers.keys():
            if biome not in MAP_DATA["noncongruent_biomes"]:
                modifier = biome_modifiers[biome]
                if modifier > MAP_DATA["biome_max"]:
                    biome_totals[biome] = MAP_DATA["biome_max"] - random.random()
                else:
                    biome_totals[biome] = modifier - random.random()

        highest = list(biome_totals.keys())[0]
        highest_at_max = []
        for total in biome_totals.keys():
            if biome_totals[total] > biome_totals[highest]:
                highest = total
            if biome_totals[total] == MAP_DATA["biome_max"]:
                highest_at_max.append(biome_totals[total])

        if len(highest_at_max) > 1:
            return highest_at_max[random.randint(0, len(highest_at_max) - 1)]
        if biome_totals[total] <= 0:
            return "desert"
        else:
            return highest


    def pick_single_biome(self, b_type, modifier = 0):

        if modifier >= MAP_DATA["congruence_max"]:
            modifier = MAP_DATA["congruence_max"]
        if random.random() <= MAP_DATA["biomes"][b_type] + modifier:
            return True
        return False

    def pick_richness(self, b_type, modifier=0):
        return 100 #NEED TO IMPLEMENT

    def check_every_direction(self, x, y, biome_modifiers):
        for x_mod in range(-1, 2):
            for y_mod in range(-1, 2):

                x_with_mod = x + x_mod
                y_with_mod = y + y_mod

                if x_with_mod >= 0 and x_with_mod <= self.height - 1 and y_with_mod >= 0 and y_with_mod <= self.width - 1:
                    biome = self.tiles[x_with_mod][y_with_mod]
                    biome_modifiers[biome.b_type] += MAP_DATA["contiguous_biomes"]
                    if biome_modifiers[biome.b_type] >= MAP_DATA["congruence_max"]:
                        biome_modifiers[biome.b_type] = MAP_DATA["congruence_max"]
                    if biome.has_river:
                        biome_modifiers["river"] += MAP_DATA["contiguous_biomes"] / 10000000

        return biome_modifiers

    def generate_map(self):
        for x in range(self.height):
            for y in range(self.width):

                if self.tiles[x][y].b_type != "water":
                    biome_modifiers = MAP_DATA["biomes"]
                    biome_modifiers = self.check_every_direction(x, y, biome_modifiers)

                    found_biome = self.pick_compare_biomes(biome_modifiers)
                    self.tiles[x][y] = biome(found_biome, self.pick_richness(found_biome))

                    if self.pick_single_biome("river"):
                        self.tiles[x][y].has_river = True

    def print_tiles(self, spacing = 10):
        for x in range(self.height):
            line_b_type = []
            line_richness = []
            line_has_river = []
            for y in range(self.width):
                biome = self.tiles[x][y]
                line_b_type.append(biome.b_type)
                line_richness.append(biome.richness)
                line_has_river.append(biome.has_river)

            line_b_type = even_spacing(line_b_type, spacing)
            line_richness = even_spacing(line_richness, spacing)
            line_has_river = even_spacing(line_has_river, spacing)

            print(line_b_type)
            print(line_richness)
            print(line_has_river)
            print("-" * spacing)


