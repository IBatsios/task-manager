🚀 Setup Instructions
1. Clone the Repository
```
git clone https://github.com/YOUR_USERNAME/task-manager.git
cd task-manager
```
2. Create a Virtual Environment (optional but recommended)
```
python -m venv venv<br>
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate        # Windows
```
3. Install Requirements
```
pip install -r requirements.txt
jupyter nbextension enable --py widgetsnbextension
```

&emsp;📦 Optional: Freeze Your Environment
```
pip freeze > requirements.txt
```
4. Run the Notebook
```
jupyter notebook
```
&emsp;&emsp;Then open the task-manager.ipynb file.<br><br>

🖥 Features<br>
&emsp;Feature	Description<br>
&emsp;&emsp;✅ Add Task	Enter task name, company, date & time<br>
&emsp;&emsp;✅ Toggle Complete	Marks task as complete/incomplete<br>
&emsp;&emsp;🗑️ Trash System	Deleted tasks go to trash.csv for recovery<br>
&emsp;&emsp;♻️ Restore from Trash	Recover accidentally deleted tasks<br>
&emsp;&emsp;🔥 Overdue Highlighting	Red bold styling on overdue, incomplete tasks<br>
&emsp;&emsp;🔍 Hide Completed	Toggle to show/hide completed tasks<br>
&emsp;&emsp;📊 Sort Columns	Sort by Task, Company, or Deadline<br>
&emsp;&emsp;📅 Google Calendar	Optional Google Calendar integration w/ reminder options<br>
&emsp;&emsp;🤫 Code Toggle Button	Toggle to show/hide code cells in notebook<br>

📂 File Structure
```
task-manager/
├── cli.py                 # CLI entry point
├── task-manager.ipynb     # Jupyter Notebook UI
├── calendar_utils.py      # Calendar integration
├── google_auth.py         # OAuth2 helper
├── task_manager.py        # Shared logic
├── tasks.csv              # Saved tasks
├── trash.csv              # Soft-deleted tasks
├── requirements.txt       # Dependencies
├── README.md
├── credentials.json       # 🔐 OAuth credentials (Git ignored)
└── token.json             # 🔐 Saved token (Git ignored)

```
🖥️ Run from Anywhere (Command Line Access)

You can make the CLI script available system-wide so you can run tasks from any terminal.
🪟 Windows
1. Create a new file called tasks.bat with the following contents:
```
@echo off
python "C:\PATH\TO\YOUR\PROJECT\task-manager\cli.py" %*
```
2. Save it in a folder already in your system `PATH`, or add the folder to your `PATH`.
&emsp;Example: `C:\Users\YourName\Scripts\` or `C:\Program Files\MyTools\`

3. Restart your terminal, then use it anywhere like:
```
tasks list
```
🐧 Linux / macOS
1. Create a new shell script called tasks:
```
#!/bin/bash
python3 /path/to/your/project/task-manager/cli.py "$@"
```
2. Make it executable:
```
chmod +x tasks
```
3. Mote it to a directory in your `PATH`, for example
```
sudo mv tasks /usr/local/bin/
```
4. Now you can run the CLI from anywhere:
```
tasks add
tasks list --hide-completed
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
🗑️ Trash Recovery

Tasks removed using destroy are not lost — they're moved to a trash.csv for recovery.
Command	Description
```
python cli.py restore	View all tasks in the trash
python cli.py restore 2	Restore trashed task #2
python cli.py restore --all	Restore all trashed tasks (with confirmation)
```

📆 Google Calendar Integration

You can now add tasks to your Google Calendar directly from the command line!
🛠️ Setup (One-Time)

    1. Enable the Google Calendar API in your Google Cloud Console
	2. Download the credentials.json file and place it in the project folder
	3. Run any --calendar command for the first time — it will open a browser to log in and authorize your Google account
	4. A token.json file will be created to store your auth session

    Security tip: Add credentials.json and token.json to your .gitignore to keep your credentials safe.

✅ Calendar Commands
Command	Description
```
python cli.py add --calendar	Adds the new task as a calendar event
python cli.py add --calendar --remind	Also adds a popup reminder 10 minutes before the task
```
📌 Example:
```
python cli.py add --task "Call Client" --company Acme --deadline "04-07 03:00 PM" --calendar --remind
```
This creates a 30-minute event in Google Calendar starting at 3:00 PM with a popup notification 10 minutes before.
🔐 Authentication Notes

    First-time use will open a browser for Google login

    You’ll only need to authorize once unless you delete token.json

    You must add yourself as a test user in the OAuth consent screen if using an unverified app

📌 Notes

    You can also use python cli.py help for quick guidance.

    Deleted tasks are moved to trash.csv — nothing is lost unless you empty the trash manually.

    Task indices (#) correspond to the list order and are used for toggling, deleting, and restoring.
    
 📓 Jupyter Notebook Features<br>
&emsp;&emsp;Visual task board with interactive widgets<br>
&emsp;&emsp;Soft-delete (Trash) with restore support<br>
&emsp;&emsp;Google Calendar integration built-in<br>
&emsp;&emsp;✅ Optional reminders like 1d, 2h, 30m, 1w, etc.<br>
&emsp;&emsp;🕓 Warns if reminder is set in the past<br>
&emsp;&emsp;📦 Task list saved in tasks.csv<br>
&emsp;&emsp;💾 Deleted tasks saved in trash.csv<br>
&emsp;&emsp;▶️ Code toggle button for clean UI<br>


📌 To use Google Calendar in notebook:
```
    Same credentials/token steps as CLI

    Check “Add to Google Calendar”

    Enter reminder offset (optional)

    Submit
```
📌 To-Do / Future Ideas
```
📱 Responsive web frontend

📤 Email task summaries

🔁 Recurring tasks

🧠 AI Smart Suggestions (grouping & deadlines)

🗓️ Export to ICS calendar format
```
🤝 Contributing

PRs welcome! If you have ideas or improvements, feel free to fork and submit a pull request.
📄 License

MIT License — do whatever you want, just give credit!
