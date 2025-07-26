# Advanced Todo List Application with File Storage

# Features:
# 1. Task Management with Categories
# 2. Due Dates
# 3. Priority Levels
# 4. Data Persistence (JSON)
# 5. Task Statistics

import json
from datetime import datetime, timedelta

class Task:
    """Represents a single task with advanced features"""
    def __init__(self, title, category="General", priority="Medium", due_date=None):
        self.title = title
        self.category = category
        self.priority = priority
        self.completed = False
        self.created_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.due_date = due_date
        self.completion_date = None

    def to_dict(self):
        """Convert task to dictionary for JSON storage"""
        return {
            "title": self.title,
            "category": self.category,
            "priority": self.priority,
            "completed": self.completed,
            "created_date": self.created_date,
            "due_date": self.due_date,
            "completion_date": self.completion_date
        }

    @classmethod
    def from_dict(cls, data):
        """Create task from dictionary"""
        task = cls(data["title"], data["category"], data["priority"], data["due_date"])
        task.completed = data["completed"]
        task.created_date = data["created_date"]
        task.completion_date = data["completion_date"]
        return task

class TodoList:
    """Advanced Todo List Manager"""
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from JSON file"""
        try:
            with open(self.filename, 'r') as file:
                data = json.load(file)
                self.tasks = [Task.from_dict(task_data) for task_data in data]
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        """Save tasks to JSON file"""
        with open(self.filename, 'w') as file:
            data = [task.to_dict() for task in self.tasks]
            json.dump(data, file, indent=4)

    def add_task(self, title, category="General", priority="Medium", due_date=None):
        """Add a new task"""
        task = Task(title, category, priority, due_date)
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{title}' added successfully!")

    def view_tasks(self, filter_completed=None, category=None, priority=None):
        """View tasks with optional filters"""
        filtered_tasks = self.tasks
        
        if filter_completed is not None:
            filtered_tasks = [t for t in filtered_tasks if t.completed == filter_completed]
        if category:
            filtered_tasks = [t for t in filtered_tasks if t.category == category]
        if priority:
            filtered_tasks = [t for t in filtered_tasks if t.priority == priority]

        if not filtered_tasks:
            print("No tasks found matching the criteria!")
            return

        print("\nTasks:")
        for i, task in enumerate(filtered_tasks, 1):
            status = "✓" if task.completed else " "
            due = f", Due: {task.due_date}" if task.due_date else ""
            print(f"{i}. [{status}] {task.title} ({task.category} - {task.priority}){due}")

    def complete_task(self, index):
        """Mark a task as completed"""
        if 1 <= index <= len(self.tasks):
            task = self.tasks[index-1]
            task.completed = True
            task.completion_date = datetime.now().strftime("%Y-%m-%d %H:%M")
            self.save_tasks()
            print(f"Task '{task.title}' marked as completed!")
        else:
            print("Invalid task number!")

    def get_statistics(self):
        """Get task statistics"""
        total_tasks = len(self.tasks)
        completed_tasks = len([t for t in self.tasks if t.completed])
        categories = {}
        priorities = {"High": 0, "Medium": 0, "Low": 0}
        
        for task in self.tasks:
            categories[task.category] = categories.get(task.category, 0) + 1
            if task.priority in priorities:
                priorities[task.priority] += 1

        print("\nTask Statistics:")
        print(f"Total Tasks: {total_tasks}")
        print(f"Completed Tasks: {completed_tasks}")
        print(f"Completion Rate: {(completed_tasks/total_tasks*100 if total_tasks else 0):.1f}%")
        print("\nTasks by Category:")
        for category, count in categories.items():
            print(f"- {category}: {count}")
        print("\nTasks by Priority:")
        for priority, count in priorities.items():
            print(f"- {priority}: {count}")

def main():
    todo_list = TodoList()
    
    while True:
        print("\n=== Advanced Todo List Manager ===")
        print("1. Add Task")
        print("2. View All Tasks")
        print("3. View Active Tasks")
        print("4. View Completed Tasks")
        print("5. Mark Task as Completed")
        print("6. View Statistics")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == "1":
            title = input("Enter task title: ")
            category = input("Enter category (press Enter for General): ") or "General"
            priority = input("Enter priority (High/Medium/Low, press Enter for Medium): ") or "Medium"
            due_date = input("Enter due date (YYYY-MM-DD, press Enter for none): ") or None
            todo_list.add_task(title, category, priority, due_date)
        
        elif choice == "2":
            todo_list.view_tasks()
        
        elif choice == "3":
            todo_list.view_tasks(filter_completed=False)
        
        elif choice == "4":
            todo_list.view_tasks(filter_completed=True)
        
        elif choice == "5":
            todo_list.view_tasks(filter_completed=False)
            task_num = input("\nEnter task number to mark as completed: ")
            try:
                todo_list.complete_task(int(task_num))
            except ValueError:
                print("Please enter a valid number!")
        
        elif choice == "6":
            todo_list.get_statistics()
        
        elif choice == "7":
            print("Thank you for using Todo List Manager!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
