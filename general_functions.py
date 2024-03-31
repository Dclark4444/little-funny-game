def even_spacing(items_to_space, width_between = 10):
    return_line = ""
    for index, item in enumerate(items_to_space):
        return_line += str(item)
        if (len(return_line) < width_between * (index + 1)):
            return_line += " " * (width_between * (index + 1) - len(return_line))

    return return_line
