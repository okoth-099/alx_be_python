# daily_reminder.py

# Step 1: Prompt for task details
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()  # Convert to lowercase for consistency
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Step 2: Process task based on priority and time sensitivity
match priority:
    case 'high':
        reminder = f"'{task}' is a high priority task"
    case 'medium':
        reminder = f"'{task}' is a medium priority task"
    case 'low':
        reminder = f"'{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an unknown priority level"

# Step 3: Modify the reminder if the task is time-sensitive
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder += ". Consider completing it when you have free time."

# Step 4: Print the customized reminder
print("\nReminder:", reminder)

