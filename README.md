# Habit-Tracker
DAY - 37/100  - Project - python X Habit Tracker via Pixela

📊 Habit Tracker via Pixela

Day 37 – 100 Days of Code Challenge

A Python-based Habit Tracker built using the Pixela REST API.
This project tracks daily habits and visualizes them as graph pixels in the browser.

🚀 Features

Create Pixela user (programmatically)

Generate custom API token

Create habit graph

Update graph details

Add daily pixel entries

Delete specific day entries

View live graph in browser

🔐 How Token & Username Work
🧑 Username

You create your own username when creating a Pixela account.

Rules:

Must start with lowercase letter

Only lowercase letters, numbers, hyphen allowed

No spaces

Example:

robin26
coding-tracker
study2026
🔑 Token (API Key)

The token is your custom secret key.

Important:

You create it manually

Pixela does NOT generate it for you

It acts like a password for API authentication

Must be kept secret

Example:

a9K2xLmP4qR8

In the script:

My_Piixela_API_Token = "YOUR_TOKEN"
My_Pixela_User_Name = "YOUR_USERNAME"

Pixela verifies every request using:

headers = {
    "X-USER-TOKEN": My_Piixela_API_Token
}
🛠 Tech Stack
Technology	Purpose
Python 3	Core language
requests	API communication
datetime	Date formatting
Pixela API	Habit tracking service
📂 Project Structure
37_HABIT_TRACKER_VIA_PIXELA.py
README.md
⚙️ Setup Instructions
1️⃣ Install dependency
pip install requests
2️⃣ Set your credentials inside the script
My_Piixela_API_Token = "YOUR_TOKEN"
My_Pixela_User_Name = "YOUR_USERNAME"
3️⃣ Run the program
python 37_HABIT_TRACKER_VIA_PIXELA.py
➕ Add Daily Pixel Example
today = datetime.now().strftime("%Y%m%d")

pixel_data = {
    "date": today,
    "quantity": input("Enter Your Total Hours: ")
}
🌐 View Your Graph

Open in browser:

https://pixe.la/v1/users/YOUR_USERNAME/graphs/graph1.html
🎯 Learning Outcomes

REST API integration

POST, PUT, DELETE requests

JSON payload handling

Token-based authentication

Date formatting for APIs

Debugging API responses

📅 Progress

Day 37 / 100 Completed ✅

⚠️ Security Note

Never upload your real API token to GitHub.
Use placeholder values before pushing your code.
