from src.ui.colorize import colorize, Color


def show_menu():
    print(f"{colorize("1.", Color.BLUE )} Create a new task")
    print(f"{colorize("2.", Color.BLUE )} Mark a task as completed")
    print(f"{colorize("3.", Color.BLUE )} Edit a pending task")
    print(f"{colorize("4.", Color.BLUE )} Show descriptions of pending tasks")
    print(f"{colorize("5.", Color.BLUE )} Show completed tasks")
    print(f"{colorize("6.", Color.BLUE )} Show pending tasks for this week")
    print(f"{colorize("7.", Color.BLUE )} Delete a pending task")
    print(f"{colorize("8.", Color.BLUE )} TEST")
    print(f"{colorize("0.", Color.BLUE )} Exit")
