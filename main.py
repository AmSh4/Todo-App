from tasks import TaskManager

def main():
    manager = TaskManager()
    while True:
        print("\n📋 To-Do List App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task description: ")
            manager.add_task(task)
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as done: "))
            manager.mark_done(task_id)
        elif choice == '4':
            task_id = int(input("Enter task ID to delete: "))
            manager.delete_task(task_id)
        elif choice == '5':
            print("Exiting To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
