class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})
        print(f"Task '{task}' added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for idx, task in enumerate(self.tasks, start=1):
                status = 'Done' if task['completed'] else 'Pending'
                print(f"{idx}. [{status}] {task['task']}")

    def mark_completed(self, task_number):
        if 1 <= task_number <= len(self.tasks):
            self.tasks[task_number - 1]['completed'] = True
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

def main():
    todo_list = TodoList()

    while True:
        print("\n=== TO-DO LIST ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            todo_list.view_tasks()
            task_number = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_completed(task_number)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
