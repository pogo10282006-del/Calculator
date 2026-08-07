# 🎓 Student Management System

A complete, professional **terminal-based Student Management System** built using **core Python only** — no external libraries, no frameworks, no OOP. Designed to be clean, modular, beginner-friendly, and crash-proof.

---

## 📌 Project Description

This project is a menu-driven console application that allows you to manage student records (Roll Number, Name, and Marks) entirely in memory during runtime. It demonstrates strong fundamentals in Python programming — functions, loops, dictionaries, lists, and robust input validation — making it an excellent addition to a beginner-to-intermediate Python portfolio.

---

## ✨ Features

1. **Add Student** — Add a student with Roll Number, Name, and Marks (0–100)
2. **View All Students** — Displays all records in a clean, aligned table
3. **Update Student** — Update name and/or marks of an existing student
4. **Delete Student** — Remove a student record with confirmation
5. **Search Student** — Search a student by Roll Number
6. **Show Topper** — Displays the student with the highest marks
7. **Calculate Average Marks** — Computes the class average
8. **Total Students** — Shows the total number of registered students
9. **Exit** — Safely exits the program

**Validation included:**
- Prevents duplicate roll numbers
- Marks must be between 0 and 100
- Names cannot be empty
- Handles invalid/non-numeric input without crashing
- Handles invalid menu selections gracefully

---

## 🛠️ Technologies Used

- **Python 3** (Standard Library only — no external packages required)

---

## 🧠 Python Concepts Used

- Functions and modular program design
- Lists and dictionaries (list of dictionaries as the data structure)
- Loops (`while`, `for`)
- Conditional statements (`if`, `elif`, `else`)
- Exception handling (`try` / `except`)
- String formatting (f-strings, alignment with format specifiers)
- Input validation and defensive programming

> Note: This project intentionally avoids Object-Oriented Programming (classes) to keep the code simple and beginner-friendly.

---

## 📁 Project Structure

```
student-management-system/
│
├── student_management_system.py   # Main application file
└── README.md                      # Project documentation
```

---

## ▶️ How to Run

### Requirements
- Python 3.7 or higher installed on your system

### Steps

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo-name>.git
   cd <your-repo-name>
   ```

2. Run the program:
   ```bash
   python student_management_system.py
   ```

3. Use the on-screen menu (1–9) to manage student records.

### Running in VS Code
1. Open the project folder in VS Code.
2. Open `student_management_system.py`.
3. Press `Ctrl + F5` (Run Without Debugging) or click the ▶️ Run button.

---

## 🚀 Future Improvements

- Save/load student data to a file (JSON or CSV) for persistent storage
- Add sorting options (by name, roll number, or marks)
- Add grade calculation based on marks (A, B, C, etc.)
- Export student records to a report file
- Add a search-by-name feature in addition to roll number
- Build a GUI version using Tkinter
- Convert into an OOP-based version using classes

---

## 👤 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [Your Name](https://linkedin.com/in/your-profile)

---

⭐ If you found this project useful, consider giving it a star on GitHub!