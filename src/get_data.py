from datetime import date
import os

COLOR_BLUE = "\033[34m"
COLOR_RESET = "\033[0m"  # Reset color
COLOR_BOLD = "\033[1m"  # Bold


def get_new_task():
    name = input(f"{COLOR_BLUE}Task name: {COLOR_RESET}")
    description = input(f"{COLOR_BLUE}Task description: {COLOR_RESET}")
    date_deadline = get_deadline()
    return name, description, date_deadline


# TODO: Works, but needs testing and further implementation
def get_selected_task(conn):
    while True:
        try:
            print("These are the stored tasks:")
            cursor = conn.cursor()
            cursor.execute("SELECT id, nombre, descripcion, fecha_limite FROM tareas")
            pending_tasks = cursor.fetchall()
            for task in pending_tasks:
                print(
                    f"{COLOR_BLUE}{task[0]}{COLOR_RESET}. {task[1]}.{COLOR_BOLD} {task[2]}{COLOR_RESET} ({task[3]})"
                )
            selection = int(input("Select the number of a task:\n"))
            found_task = None
            for task in pending_tasks:
                if task[0] == selection:
                    found_task = task
                    break
            if found_task is None:
                raise ValueError("The selected task is not in the list")
            print(
                f"The task found is number {found_task[0]}: {found_task[1]}"
            )
            return found_task
        except ValueError as e:
            os.system("clear")
            print(f"Error: {e}. Please enter a valid task")


def get_deadline():
    today = date.today()
    print(f"Today is {today.strftime('%B')} {today.day}, {today.year}")

    while True:
        try:
            day_deadline = int(input(f"{COLOR_BLUE}Deadline: \n\tDay: {COLOR_RESET}"))
            if not 1 <= day_deadline <= 31:
                raise ValueError("The day must be between 1 and 31")

            month_deadline = int(input(f"{COLOR_BLUE}\tMonth: {COLOR_RESET}"))
            if not 1 <= month_deadline <= 12:
                raise ValueError("The month must be between 1 and 12")

            year_deadline = int(input(f"{COLOR_BLUE}\tYear: {COLOR_RESET}"))
            if year_deadline < 2024:
                raise ValueError("The year must be 2024 or later")
            date_deadline = date(year_deadline, month_deadline, day_deadline)
            if date_deadline == today:
                print("It's for today!")
            elif date_deadline < today:
                print("That date has already passed! Enter a valid date")
                continue
            else:
                print(
                    f"Task scheduled for {date_deadline.day} of {date_deadline.month} of {date_deadline.year}"
                )
            formated_date_deadline = f"{day_deadline}/{month_deadline}/{year_deadline}"
            return formated_date_deadline
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid date.")
