# 📝 Todo CLI App (Python)

A simple command-line todo list manager written in Python.  
This app allows you to manage your tasks with priority levels and deadlines, and keeps track of their completion status.

---

## 📦 Features

- ✅ Add todos with:
  - Unique ID
  - Priority (`High`, `Medium`, `Low`)
  - Deadline (`YYYY-MM-DD`)
- 🗒 View todos sorted by:
  - Priority
  - Upcoming deadlines
- ✏️ Change the status of a todo (done / not done)
- 🗑 Remove todos
- 💾 All data is saved to a local text file `todo.txt`

---

## 🚀 Getting Started

### Requirements

- Python 3.7 or higher

### Running the App

1. Clone or download this repository.
2. Open your terminal and navigate to the project directory.
3. Run the script:

```bash
python todo.py
```

## 📋 Usage

### After launching the app, you’ll see the main menu:

Options:
  1 - add todo
  2 - show todos
  3 - remove todo
  4 - change status to done
  5 - change status to not done
  6 - sorted by upcoming deadline
  0 - quit


##  🔹 Add a Todo


You will be prompted to:
	1.	Enter a title
	2.	Select a priority:
	•	1 = 🔴 High
	•	2 = 🟡 Medium
	•	3 = 🟢 Low
	3.	Enter a deadline in the format YYYY-MM-DD

Example:

  Input todo title: Finish report

  Select priority:
    1 - 🔴 High
    2 - 🟡 Medium
    3 - 🟢 Low
  Input priority(1-3): 1

  Enter deadline (in YYYY-MM-DD format): 2025-08-15


##  🔄 Change Status

Choose option 4 or 5 and input the todo ID when prompted.
	•	4 – Mark as done
	•	5 – Mark as not done



🗑 Remove a Todo

Choose option 3 and enter the todo ID you want to delete.

⸻

📆 View Upcoming Todos

Choose option 6 to view todos sorted by the nearest deadline.

⸻

🗃 Data Format

All todos are stored in a local file todo.txt.
Each line represents one todo item with the following format:
<pre>
```text
&lt;id&gt;|&lt;title&gt;|&lt;priority&gt;|&lt;status&gt;|&lt;deadline&gt;
```
</pre>

Example:

<pre>
```text
82765|Pay bills|high|False|2025-08-10
10923|Write article|medium|True|2025-08-12
```
</pre>

•	id – auto-generated unique string
•	status – True if completed, False otherwise



🛠 Technologies Used
	•	Python Standard Library:
	•	os – for file path handling
	•	random – for ID generation
	•	time – for timestamp in IDs
	•	datetime – for deadline parsing and comparison


📄 License

This project is open-source and available under the MIT License.


🙌 Author

Created by Serhii Tustanovskyi

Feel free to fork, contribute, and share!