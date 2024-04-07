def even_spacing(items_to_space, width_between = 10):
    return_line = ""
    for index, item in enumerate(items_to_space):
        return_line += str(item)
        if (len(return_line) < width_between * (index + 1)):
            return_line += " " * (width_between * (index + 1) - len(return_line))

    return return_line


def get_river_overlay(x_coord, y_coord, tiles):
    tile_index = 0
    tile_indexes_needed = []

    for x_mod in range(-1, 2):
        for y_mod in range(-1, 2):

            if x_mod != 0 and y_mod != 0 or x_mod == -1 and y_mod == 0 or x_mod == 1 and y_mod == 0:

                if x_mod + x_coord < len(tiles) - 1 and y_mod + y_coord < len(tiles[0]) - 1 and tiles[x_coord + x_mod][y_coord + y_mod].has_river:
                    tile_indexes_needed.append(tile_index)

                tile_index += 1

    if tile_indexes_needed == []:
        tile_indexes_needed = [6]
    return tile_indexes_needed


