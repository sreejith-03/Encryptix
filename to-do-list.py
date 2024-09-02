class ToDoList:
    def __init__(self):
        self.tasks = []

    def display_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("\nYour To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                status = "Done" if task['completed'] else "Not Done"
                print(f"{index}. {task['task']} - {status}")

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Added task: '{task}'")

    def update_task(self, task_number, new_task):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["task"] = new_task
            print(f"Task {task_number} updated to: '{new_task}'")
        else:
            print("Invalid task number.")

    def mark_task_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed.")
        else:
            print("Invalid task number.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Deleted task: '{removed_task['task']}'")
        else:
            print("Invalid task number.")

    def menu(self):
        while True:
            print("\nTo-Do List Menu:")
            print("1. View Tasks")
            print("2. Add Task")
            print("3. Update Task")
            print("4. Mark Task as Completed")
            print("5. Delete Task")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")
            
            if choice == '1':
                self.display_tasks()
            elif choice == '2':
                task = input("Enter the task: ")
                self.add_task(task)
            elif choice == '3':
                task_number = int(input("Enter the task number to update: "))
                new_task = input("Enter the new task: ")
                self.update_task(task_number, new_task)
            elif choice == '4':
                task_number = int(input("Enter the task number to mark as completed: "))
                self.mark_task_completed(task_number)
            elif choice == '5':
                task_number = int(input("Enter the task number to delete: "))
                self.delete_task(task_number)
            elif choice == '6':
                print("Exiting the To-Do List application.")
                break
            else:
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    todo_list = ToDoList()
    todo_list.menu()
