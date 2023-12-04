# To-Do List in Python

# Initialize an empty list to store tasks
tasks = []

while True:
    # Display menu
    print("\n===== To-Do List Menu =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Quit")

    # Get user input
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        # Add task
        task = input("Enter the task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == "2":
        # View tasks
        if tasks:
            print("\n===== Your To-Do List =====")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("Your to-do list is empty.")

    elif choice == "3":
        # Mark task as completed
        if tasks:
            print("\n===== Your To-Do List =====")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            task_index = int(input("Enter the task number to mark as completed: "))
            if 1 <= task_index <= len(tasks):
                del tasks[task_index - 1]
                print("Task marked as completed!")
            else:
                print("Invalid task number.")
        else:
            print("Your to-do list is empty.")

    elif choice == "4":
        # Delete task
        if tasks:
            print("\n===== Your To-Do List =====")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            task_index = int(input("Enter the task number to delete: "))
            if 1 <= task_index <= len(tasks):
                del tasks[task_index - 1]
                print("Task deleted successfully!")
            else:
                print("Invalid task number.")
        else:
            print("Your to-do list is empty.")

    elif choice == "5":
        # Quit
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")