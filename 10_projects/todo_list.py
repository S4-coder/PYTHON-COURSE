# To-Do List Application

class TodoList:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added successfully!")
    
    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list!")
            return
        
        print("\nYour To-Do List:")
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else " "
            print(f"{i}. [{status}] {task['task']}")
    
    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index-1]["completed"] = True
            print(f"Task '{self.tasks[task_index-1]['task']}' marked as completed!")
        else:
            print("Invalid task number!")
    
    def remove_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            removed_task = self.tasks.pop(task_index-1)
            print(f"Task '{removed_task['task']}' removed successfully!")
        else:
            print("Invalid task number!")

def main():
    todo_list = TodoList()
    
    while True:
        print("\n=== To-Do List Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Remove Task")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ")
        
        if choice == "1":
            task = input("Enter task description: ")
            todo_list.add_task(task)
        
        elif choice == "2":
            todo_list.view_tasks()
        
        elif choice == "3":
            todo_list.view_tasks()
            task_num = input("\nEnter task number to mark as completed: ")
            try:
                todo_list.mark_completed(int(task_num))
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice == "4":
            todo_list.view_tasks()
            task_num = input("\nEnter task number to remove: ")
            try:
                todo_list.remove_task(int(task_num))
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice == "5":
            print("Thank you for using To-Do List Manager!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
