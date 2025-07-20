# 🗂️ File Auto-Organiser

A Python tool that generates fake business files and automatically organises them into folders based on file type.

---

## 🚀 Features
- 📄 Generates 100 fake business files with random names and extensions.
- 🗂 Automatically organises files into categories (Legal, Financials, Marketing, Reports, Communications).
- 🔥 Handles existing folders and avoids overwriting.

---

## 📂 Project Structure
file-auto-organiser/
├── generate_files.py # Script to create fake files
├── organize_files.py # Script to sort files into folders
└── README.md # Project documentation

yaml
Copy code

---

## ⚙️ How to Use

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/file-auto-organiser.git
cd file-auto-organiser
2️⃣ Run generate_files.py
Generates 100 random files in the business-folder:

bash
Copy code
python generate_files.py
3️⃣ Run organize_files.py
Sorts the files into folders based on their extension:

bash
Copy code
python organize_files.py
✨ Customisation
Edit file_types in organize_files.py to define your own folder categories.

Change folder in generate_files.py to use a different folder.

👨‍💻 Author
Developed by Somtochukwu O
