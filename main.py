from notion_client import Client
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Notion client
notion = Client(auth=os.getenv("NOTION_API_KEY"))
DATABASE_ID = os.getenv("NOTION_DATABASE_ID")

# Add a task
def add_task(task_name):
    try:
        notion.pages.create(
            parent={"database_id": DATABASE_ID},
            properties={
                "Name": {"title": [{"text": {"content": task_name}}]},
                "Status": {"status": {"name": "Not started"}}  
            }
        )
        print(f"Added: {task_name}")
    except Exception as e:
        print(f"Error details: {e.body}") 
        print(f"Failed to add task: {e}")

# Get all tasks
def get_tasks():
    try:
        response = notion.databases.query(database_id=DATABASE_ID)
        tasks = response["results"]
        for i, task in enumerate(tasks):
            name = task["properties"]["Name"]["title"][0]["text"]["content"]
            status = task["properties"]["Status"]["status"]["name"]  
            print(f"{i + 1}. {name} (Status: {status})")
        return tasks
    except Exception as e:
        print(f"Failed to fetch tasks: {e}")
        return []

# Update a task's status
def update_task(task_id, new_status):
    try:
        notion.pages.update(
            page_id=task_id,
            properties={
                "Status": {"status": {"name": new_status}}  
            }
        )
        print(f"Updated task to: {new_status}")
    except Exception as e:
        print(f"Failed to update task: {e}")


def main():
    while True:
        print("\n--- Notion To-Do List ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Update Task Status")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1": 
            print("\nYour Tasks:")
            get_tasks()

        elif choice == "2":  
            task_name = input("Enter task name: ").strip()
            if task_name:
                add_task(task_name)
            else:
                print("Task name cannot be empty.")

        elif choice == "3":  
            tasks = get_tasks()
            if tasks:
                try:
                    task_num = int(input("Enter task number to update: ")) - 1
                    if 0 <= task_num < len(tasks):
                        new_status = input("Enter new status ('Not started', 'In progress', 'Done'): ").strip()
                        if new_status in ["Not started", "In progress", "Done"]:  
                            task_id = tasks[task_num]["id"]
                            update_task(task_id, new_status)
                        else:
                            print("Invalid status. Please use one of: 'Not started', 'In progress', 'Done'.")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Invalid input. Please enter a valid task number.")
            else:
                print("No tasks found.")

        elif choice == "4":  
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()