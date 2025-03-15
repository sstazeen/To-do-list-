import sqlite3
import datetime
from tabulate import tabulate

def create_table():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS tasks
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                      user_task TEXT, 
                      deadline TEXT, 
                      status TEXT DEFAULT 'Pending')''')
    conn.commit()
    conn.close()

def add_task(user_task, deadline):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (user_task, deadline) VALUES (?, ?)", (user_task, deadline))
    conn.commit()
    conn.close()

def view_tasks():
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def delete_task(task_id):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def mark_task_completed(task_id):
    conn = sqlite3.connect("todo.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = 'Completed' WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

def main():
    create_table()
    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")
        
        choice = input("Enter choice: ")
        
        if choice == "1":
            user_task = input("Enter task: ")
            deadline = input("Enter due date (YYYY-MM-DD): ")
            add_task(user_task, deadline)
            print("Task added successfully!")
        elif choice == "2":
            tasks = view_tasks()
            if tasks:
                print(tabulate(tasks, headers=["ID", "Task", "Due Date", "Status"], tablefmt="fancy_grid"))
            else:
                print("No tasks found.")
        elif choice == "3":
            task_id = input("Enter task ID to delete: ")
            delete_task(task_id)
            print("Task deleted successfully!")
        elif choice == "4":
            task_id = input("Enter task ID to mark as completed: ")
            mark_task_completed(task_id)
            print("Task marked as completed!")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
