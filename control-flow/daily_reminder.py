#Personal Daily Remainder app

task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        remainder = f"Reminder: {task} is a high priority task"
    case "medium":
        remainder = f"Reminder: {task} is a medium priority task"
    case "low":
        remainder = f"Note: {task} is a low priority task."
    case _:
        remainder = f"{task} is of unknown priority"

if time_bound == yes:
    print(f"{remainder} that requires immediate attention today!")
else:
    print(f"{remainder} Consider completing it when you have free time.")
