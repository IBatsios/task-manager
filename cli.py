import pandas as pd
import os
from datetime import datetime
import argparse
from colorama import init, Fore, Style
init(autoreset=True)
from calendar_utils import add_event_to_calendar

# Ensure it always loads from script directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

TASKS_FILE = "tasks.csv"
TRASH_FILE = "trash.csv"

def toggle_task(index):
    df = load_tasks()
    if index < 0 or index >= len(df):
        print(f"Invalid index: {index}")
        return

    df.at[index, "Completed"] = not df.at[index, "Completed"]
    save_tasks(df)
    status = "completed" if df.at[index, "Completed"] else "incomplete"
    print(f"✅ Task {index} marked as {status}.")

def load_tasks():
    try:
        return pd.read_csv(TASKS_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Completed", "Task", "Company", "Deadline"])

def save_tasks(df):
    df.to_csv(TASKS_FILE, index=False)

def list_tasks(sort_by="deadline", view=None, hide_completed=False):
    df = load_tasks()  # ✅ Load at the top

    if df.empty:
        print("No tasks found.")
        return

    df["Deadline"] = pd.to_datetime(df["Deadline"], errors="coerce")

    if hide_completed:
        df = df[df["Completed"] == False]
        
    # Column widths
    DONE_WIDTH = 6
    TASK_WIDTH = 40
    COMPANY_WIDTH = 22
    DEADLINE_WIDTH = 15

    # Total width for divider
    TABLE_WIDTH = DONE_WIDTH + TASK_WIDTH + COMPANY_WIDTH + DEADLINE_WIDTH + 6  # 6 = spacing buffers

    if df.empty:
        print("No tasks found.")
        return

    df["Deadline"] = pd.to_datetime(df["Deadline"], errors="coerce")

    if view:
        valid_views = ["task", "company", "deadline"]
        view = view.lower()
        if view not in valid_views:
            print(f"Invalid --view option: {view}")
            return
        print(f"\n📄 Viewing unique {view}s:\n")
        print(df[view.capitalize()].dropna().drop_duplicates().sort_values().to_string(index=False))
        return

    # Sort normally if no --view
    valid_sorts = {
        "task": "Task",
        "company": "Company",
        "deadline": "Deadline",
        "#": None
    }
    if sort_by.lower() == "#":
        df = df.reset_index()  # use old index as column named "index"
        df = df.rename(columns={"index": "#"})
        sort_column = "#"
        df = df.sort_values(by="#")
    else:
        sort_column = valid_sorts.get(sort_by.lower(), "Deadline")
        df = df.sort_values(by=sort_column)

    print(f"\n📋 Tasks (sorted by {sort_column}):\n")
    
    # Table header
    print(f"{'#':<4} {'Done':<{DONE_WIDTH}} {'Task':<{TASK_WIDTH}} {'Company':<{COMPANY_WIDTH}} {'Deadline':<{DEADLINE_WIDTH}}")
    print("-" * TABLE_WIDTH)

    for i, row in df.iterrows():
        completed = row["Completed"]
        deadline = pd.to_datetime(row["Deadline"])
        is_overdue = not completed and deadline < datetime.now()

        # Truncate long text to column widths
        task = str(row["Task"])[:TASK_WIDTH - 1]
        company = str(row["Company"])[:COMPANY_WIDTH - 1]
        deadline_str = deadline.strftime("%m-%d %I:%M %p")

        # Colors
        if completed:
            color = Fore.GREEN
        elif is_overdue:
            color = Fore.RED
        else:
            color = ""

        print(
            f"{i:<4} {'✓' if completed else ' ':<{DONE_WIDTH}} "
            f"{color}{task:<{TASK_WIDTH}} "
            f"{company:<{COMPANY_WIDTH}} "
            f"{deadline_str:<{DEADLINE_WIDTH}}{Style.RESET_ALL}"
        )

def add_task(args):
    task = args.task or input("Task name: ").strip()
    company = args.company or input("Company: ").strip()
    deadline_input = args.deadline or input("Deadline (MM-DD HH:MM AM/PM): ").strip()

    year = datetime.now().year
    try:
        deadline = pd.to_datetime(f"{year}-{deadline_input}")
    except Exception as e:
        print(f"Invalid deadline format: {e}")
        return

    df = load_tasks()
    df.loc[len(df)] = [False, task, company, deadline]
    save_tasks(df)
    print("✅ Task added successfully!")

    # Add to Google Calendar if requested
    if args.calendar:
        try:
            add_event_to_calendar(task, company, deadline, reminder=args.remind)
        except Exception as e:
            print(f"⚠️  Could not add to calendar: {e}")
    
def destroy_task(index=None, delete_all=False):
    df = load_tasks()

    if delete_all:
        if df.empty:
            print("📂 No tasks to delete.")
            return

        confirm = input("⚠️  This will permanently delete ALL tasks. Continue? (y/n): ").strip().lower()
        if confirm != "y":
            print("🛑 Deletion cancelled.")
            return

        for _, row in df.iterrows():
            move_to_trash(row)

        save_tasks(pd.DataFrame(columns=["Completed", "Task", "Company", "Deadline"]))
        print("🧨 All tasks moved to trash.")
        return

    # Delete one task by index
    if index is None:
        print("❌ Please provide a task index or use --all.")
        return

    if index < 0 or index >= len(df):
        print(f"❌ Invalid index: {index}")
        return

    deleted = df.loc[index]

    confirm = input(f"⚠️  Are you sure you want to delete task {index} — \"{deleted['Task']}\"? (y/n): ").strip().lower()
    if confirm != "y":
        print("🛑 Deletion cancelled.")
        return

    move_to_trash(deleted)
    df = df.drop(index).reset_index(drop=True)
    save_tasks(df)
    print(f"🗑️ Task {index} moved to trash: \"{deleted['Task']}\"")
    
def move_to_trash(row):
    try:
        trash_df = pd.read_csv(TRASH_FILE)
    except FileNotFoundError:
        trash_df = pd.DataFrame(columns=["Completed", "Task", "Company", "Deadline"])

    trash_df = pd.concat([trash_df, pd.DataFrame([row])], ignore_index=True)
    trash_df.to_csv(TRASH_FILE, index=False)
    
def load_trash():
    try:
        return pd.read_csv(TRASH_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Completed", "Task", "Company", "Deadline"])
    
def restore_task(index=None, restore_all=False):
    trash_df = load_trash()
    if trash_df.empty:
        print("🧺 Trash is empty.")
        return

    if restore_all:
        confirm = input("⚠️  This will restore ALL tasks from trash. Continue? (y/n): ").strip().lower()
        if confirm != "y":
            print("🛑 Restore cancelled.")
            return

        df = load_tasks()
        df = pd.concat([df, trash_df], ignore_index=True)
        save_tasks(df)

        # Clear the trash
        trash_df = pd.DataFrame(columns=["Completed", "Task", "Company", "Deadline"])
        trash_df.to_csv(TRASH_FILE, index=False)

        print("✅ All trashed tasks have been restored.")
        return

    if index is None:
        print("\n🧺 Trash:")
        print(f"{'#':<4} {'Task':<30} {'Company':<20} {'Deadline'}")
        print("-" * 70)
        for i, row in trash_df.iterrows():
            deadline = pd.to_datetime(row["Deadline"]).strftime("%m-%d %I:%M %p")
            print(f"{i:<4} {row['Task']:<30} {row['Company']:<20} {deadline}")
        return

    if index < 0 or index >= len(trash_df):
        print(f"❌ Invalid index: {index}")
        return

    row = trash_df.loc[index]
    df = load_tasks()
    df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    save_tasks(df)

    # Remove from trash
    trash_df = trash_df.drop(index).reset_index(drop=True)
    trash_df.to_csv(TRASH_FILE, index=False)

    print(f"✅ Restored task: \"{row['Task']}\"")



def main():
    parser = argparse.ArgumentParser(description="📋 Task Manager CLI")

    subparsers = parser.add_subparsers(dest="command", required=True)

    # list command
    list_parser = subparsers.add_parser("list", help="Show all tasks")
    list_parser.add_argument(
        "--sort", choices=["task", "company", "deadline", "#"],
        default="#",
        help='Sort tasks by this field (default: "#")' 
    )
    list_parser.add_argument("--view", choices=["task", "company", "deadline"], help="View unique values for a specific column")
    list_parser.add_argument("--hide-completed", action="store_true", help="Hide completed tasks")

    # add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("--task", type=str, help="Task name")
    add_parser.add_argument("--company", type=str, help="Company name")
    add_parser.add_argument("--deadline", type=str, help='Deadline in "MM-DD HH:MM AM/PM" format')
    add_parser.add_argument("--calendar", action="store_true", help="Also add this task to your Google Calendar")
    add_parser.add_argument("--remind", action="store_true", help="Add a popup reminder 10 minutes before event")
  
    # destroy command
    destroy_parser = subparsers.add_parser("destroy", help="Delete task(s)")
    destroy_parser.add_argument("index", type=int, nargs="?", help="Index of task to delete")
    destroy_parser.add_argument("--all", action="store_true", help="Delete ALL tasks")
    
    # restore command
    restore_parser = subparsers.add_parser("restore", help="View or restore tasks from trash")
    restore_parser.add_argument("index", type=int, nargs="?", help="Index of task in trash to restore")
    restore_parser.add_argument("--all", action="store_true", help="Restore ALL tasks from trash")

    # toggle command
    toggle_parser = subparsers.add_parser("toggle", help="Toggle completion status of a task")
    toggle_parser.add_argument("index", type=int, help="Index of task to toggle")

    # Help alias
    import sys
    if len(sys.argv) >= 2 and sys.argv[1].lower() == "help":
        sys.argv[1] = "--help"

    args = parser.parse_args()

    if args.command == "list":
        list_tasks(sort_by=args.sort, view=args.view, hide_completed=args.hide_completed)
    elif args.command == "add":
        add_task(args)
    elif args.command == "destroy":
        destroy_task(index=args.index, delete_all=args.all)
    elif args.command == "restore":
        restore_task(index=args.index, restore_all=args.all)
    elif args.command == "toggle":
        toggle_task(args.index)

if __name__ == "__main__":
    main()
