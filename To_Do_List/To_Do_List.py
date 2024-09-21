import json
import os

FILE_PATH = 'tasks.json'

def load_tasks():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(FILE_PATH, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, title, description):
    tasks.append({'title': title, 'description': description, 'status': 'Pending'})
    save_tasks(tasks)

def update_task(tasks, index, title=None, description=None, status=None):
    if title:
        tasks[index]['title'] = title
    if description:
        tasks[index]['description'] = description
    if status:
        tasks[index]['status'] = status
    save_tasks(tasks)

def delete_task(tasks, index):
    tasks.pop(index)
    save_tasks(tasks)

def view_tasks(tasks):
    for idx, task in enumerate(tasks):
        print(f"Task {idx + 1}:")
        print(f"  Title: {task['title']}")
        print(f"  Description: {task['description']}")
        print(f"  Status: {task['status']}")
        print()

def main():
    tasks = load_tasks()
    while True:
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            add_task(tasks, title, description)
        elif choice == '2':
            index = int(input("Enter task number to update: ")) - 1
            title = input("Enter new task title (leave blank to keep current): ")
            description = input("Enter new task description (leave blank to keep current): ")
            status = input("Enter new task status (leave blank to keep current): ")
            update_task(tasks, index, title, description, status)
        elif choice == '3':
            index = int(input("Enter task number to delete: ")) - 1
            delete_task(tasks, index)
        elif choice == '4':
            view_tasks(tasks)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
