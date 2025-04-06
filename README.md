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

```task-manager/
├── task-manager.ipynb     # Jupyter interface
├── task_manager.py        # (Optional) Logic helper module
├── tasks.csv              # Stores task list (auto-created)
├── README.md              # This file
└── requirements.txt       # Optional pip requirements
```

📌 To-Do / Coming Soon

    ☁️ Google Calendar integration

    🖥️ CLI tool (tasks, tasks -add, tasks -all)

    📱 Responsive version or web-based frontend

🤝 Contributing

PRs welcome! If you have ideas or improvements, feel free to fork and submit a pull request.
📄 License

MIT License — do whatever you want, just give credit!
