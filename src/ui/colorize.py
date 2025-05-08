COLORS = {
    "RESET": "\033[0m",
    "BLUE": "\033[34m",
    "BLUE_TITLE": "\033[34;1;4m",
    "WHITE": "\033[37m",
    "BOLD": "\033[1m",
}


def colorize(text: str, *color_keys: str):
    color_codes = "".join(COLORS.get(key, "") for key in color_keys)
    return f"{color_codes}{text}{COLORS["RESET"]}"
