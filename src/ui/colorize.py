from enum import Enum


class Color(str, Enum):
    RESET = ("\033[0m",)
    BLUE = ("\033[34m",)
    BLUETITLE = ("\033[34;1;4m",)
    WHITE = ("\033[37m",)
    BOLD = ("\033[1m",)
    RED = ("\033[31m",)


def colorize(text: str, color: Color):
    return f"{color.value}{text}{Color.RESET.value}"
