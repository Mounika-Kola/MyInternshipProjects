class Task:
    def __init__(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date, priority):
        task = Task(description, due_date, priority)
        self.tasks.append(task)

    def display_tasks(self):
        for i, task in enumerate(self.tasks, start=1):
            status = "Completed" if task.completed else "Not Completed"
            print(f"{i}. Description: {task.description}, Due Date: {task.due_date}, Priority: {task.priority}, Status: {status}")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True

    def update_task(self, task_index, description, due_date, priority):
        if 1 <= task_index <= len(self.tasks):
            task = self.tasks[task_index - 1]
            task.description = description
            task.due_date = due_date
            task.priority = priority

    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]

if __name__ == "__main__":
    to_do_list = ToDoList()

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. Display Tasks")
        print("3. Mark Task as Completed")
        print("4. Update Task")
        print("5. Remove Task")
        print("6. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            due_date = input("Enter due date: ")
            priority = input("Enter priority: ")
            to_do_list.add_task(description, due_date, priority)
        elif choice == "2":
            to_do_list.display_tasks()
        elif choice == "3":
            task_index = int(input("Enter the task number to mark as completed: "))
            to_do_list.mark_completed(task_index)
        elif choice == "4":
            task_index = int(input("Enter the task number to update: "))
            description = input("Enter new description: ")
            due_date = input("Enter new due date: ")
            priority = input("Enter new priority: ")
            to_do_list.update_task(task_index, description, due_date, priority)
        elif choice == "5":
            task_index = int(input("Enter the task number to remove: "))
            to_do_list.remove_task(task_index)
        elif choice == "6":
            break

        else:
            print("Invalid choice. Please try again.")
