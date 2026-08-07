import json
import os
from datetime import datetime
 
DATA_FILE = "tasks.json"
 
 
def load_tasks():
    """Load tasks from the JSON file. Returns an empty list if none exist."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []
 
 
def save_tasks(tasks):
    """Save the list of tasks to the JSON file."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)
 
 
def add_task(tasks):
    task_text = input("Enter the task: ").strip()
    if not task_text:
        print("⚠️  Task cannot be empty.\n")
        return
    tasks.append({
        "task": task_text,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M")
    })
    save_tasks(tasks)
    print(f"✅ Added: '{task_text}'\n")
 
 
def view_tasks(tasks):
    if not tasks:
        print("📭 No tasks yet. Add one!\n")
        return
    print("\n📋 Your To-Do List:")
    print("-" * 40)
    for i, t in enumerate(tasks, start=1):
        status = "✔️ Done" if t["done"] else "❌ Pending"
        print(f"{i}. [{status}] {t['task']}  (added {t['created']})")
    print("-" * 40 + "\n")
 
 
def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num - 1]["done"] = True
            save_tasks(tasks)
            print(f"🎉 Marked '{tasks[num - 1]['task']}' as done.\n")
        else:
            print("⚠️  Invalid task number.\n")
    except ValueError:
        print("⚠️  Please enter a valid number.\n")
 
 
def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"🗑️  Deleted: '{removed['task']}'\n")
        else:
            print("⚠️  Invalid task number.\n")
    except ValueError:
        print("⚠️  Please enter a valid number.\n")
 
 
def print_menu():
    print("=" * 40)
    print("           📝 TO-DO LIST APP")
    print("=" * 40)
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")
    print("=" * 40)
 
 
def main():
    tasks = load_tasks()
 
    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()
 
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Goodbye! Your tasks have been saved.")
            break
        else:
            print("⚠️  Invalid choice, please enter a number from 1-5.\n")
 
 
if __name__ == "__main__":
    main()