🚀 Setup Instructions
1. Clone the Repository

&emsp;&emsp;git clone https://github.com/YOUR_USERNAME/task-manager.git<br>
&emsp;&emsp;cd task-manager<br>


2. Create a Virtual Environment (optional but recommended)

&emsp;&emsp;python -m venv venv<br>
&emsp;&emsp;source venv/bin/activate     # macOS/Linux<br>
&emsp;&emsp;venv\Scripts\activate        # Windows<br>

3. Install Requirements

&emsp;&emsp;pip install -r requirements.txt<br>
&emsp;&emsp;jupyter nbextension enable --py widgetsnbextension<br>

&emsp;📦 Optional: Freeze Your Environment

&emsp;&emsp;pip freeze > requirements.txt

4. Run the Notebook

&emsp;&emsp;jupyter notebook

&emsp;&emsp;Then open the task-manager.ipynb file.<br><br>

🖥 Features<br>
&emsp;Feature	Description<br>
&emsp;&emsp;✅ Add Task	Enter task name, company, date & time<br>
&emsp;&emsp;✅ Toggle Complete	Marks task as complete or incomplete<br>
&emsp;&emsp;🗑️ Delete Task	Removes task from list and file<br>
&emsp;&emsp;🔥 Overdue Highlighting	Red bold styling on overdue, incomplete tasks<br>
&emsp;&emsp;🔍 Hide Completed	Toggle to hide/show completed tasks<br>
&emsp;&emsp;📊 Sort Columns	Click column headers to sort by Task, Company, or Deadline<br>

📂 File Structure
```
task-manager/
├── cli.py                 # ✅ New CLI tool
├── task-manager.ipynb
├── task_manager.py        # (shared logic if needed)
├── tasks.csv
├── README.md
└── requirements.txt
```

🧑‍💻 Command Line Interface (CLI)

Manage your tasks directly from the terminal with powerful commands:<br>
✅ Basic Commands
Command	Description
```
python cli.py list	View tasks sorted by # (default)
python cli.py list --sort task	Sort tasks by task name
python cli.py list --view company	View unique companies
python cli.py list --hide-completed	Hide completed tasks from view
python cli.py add	Add a new task (interactive or with flags)
python cli.py toggle 3	Toggle completion status of task #3
python cli.py destroy 3	Move task #3 to trash
python cli.py destroy --all	Move all tasks to trash (with confirmation)
```
🗑️ Trash Management

Tasks removed using destroy are not lost — they're moved to a trash.csv for recovery.
Command	Description
```
python cli.py restore	View all tasks in the trash
python cli.py restore 2	Restore trashed task #2
python cli.py restore --all	Restore all trashed tasks (with confirmation)
```
📌 Notes

    You can also use python cli.py help for quick guidance.

    Deleted tasks are moved to trash.csv — nothing is lost unless you empty the trash manually.

    Task indices (#) correspond to the list order and are used for toggling, deleting, and restoring.

📌 To-Do / Coming Soon

    ☁️ Google Calendar integration

    📱 Responsive version or web-based frontend

🤝 Contributing

PRs welcome! If you have ideas or improvements, feel free to fork and submit a pull request.
📄 License

MIT License — do whatever you want, just give credit!
