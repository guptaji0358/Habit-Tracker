# Habit-Tracker
DAY - 37/100  - Project - python X Habit Tracker via Pixela

📊 Habit Tracker via Pixela (Day 37)

A Python-based Habit Tracker built using the Pixela API as part of the 100 Days of Code – Python Bootcamp.

🚀 Features

Create Pixela User

Create Graph

Update Graph

Add Daily Pixel

Delete Pixel

View Graph in Browser

Token-Based Authentication

🛠 Tech Stack

Python 3

requests

datetime

REST API (Pixela)

📂 Project Structure
.
├── 37_HABIT_TRACKER_VIA_PIXELA.py
└── README.md
⚙️ Setup Instructions
1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
2. Install dependency
pip install requests
3. Add your credentials inside the script
My_Piixela_API_Token = "YOUR_TOKEN"
My_Pixela_User_Name = "YOUR_USERNAME"
4. Run the script
python 37_HABIT_TRACKER_VIA_PIXELA.py
📈 Create Graph Example
graph_config = {
    "id": "graph1",
    "name": "Python Coding Tracker",
    "unit": "hours",
    "type": "int",
    "color": "ajisai"
}
➕ Add Daily Pixel
today = datetime.now().strftime("%Y%m%d")

pixel_data = {
    "date": today,
    "quantity": input("Enter Your Total Hours: ")
}
🌐 View Your Graph

Open in browser:

https://pixe.la/v1/users/YOUR_USERNAME/graphs/graph1.html
🎯 Learning Outcomes

Understanding REST APIs

Working with POST, PUT, DELETE

Handling JSON data

Token authentication

Date formatting

Debugging API responses

📅 Progress

Day 37 / 100 Completed ✅

🔐 Security Note

Do NOT upload your real API token to GitHub.
Use environment variables for production-level security.
