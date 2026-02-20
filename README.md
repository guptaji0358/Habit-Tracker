# Habit-Tracker
DAY - 37/100  - Project - python X Habit Tracker via Pixela

📊 Habit Tracker via Pixela

Day 37 – 100 Days of Code Challenge

A Python-based Habit Tracker built using the Pixela REST API.
This project logs daily habits as graph pixels and visualizes progress in the browser.

🚀 Features

✔ Create Pixela user
✔ Create habit graph
✔ Update graph properties
✔ Add daily pixel entries
✔ Delete specific day entries
✔ View live graph in browser
✔ Token-based authentication

🛠 Tech Stack
Technology	Purpose
Python 3	Core programming language
requests	API communication
datetime	Date formatting
Pixela API	Habit visualization
📂 Project Structure
37_HABIT_TRACKER_VIA_PIXELA.py
README.md
⚙️ How To Run
1️⃣ Install dependency
pip install requests
2️⃣ Add your credentials

Inside the script:

My_Piixela_API_Token = "YOUR_TOKEN"
My_Pixela_User_Name = "YOUR_USERNAME"
3️⃣ Run the program
python 37_HABIT_TRACKER_VIA_PIXELA.py
📈 Example Pixel Entry
today = datetime.now().strftime("%Y%m%d")

pixel_data = {
    "date": today,
    "quantity": input("Enter Your Total Hours: ")
}
🌐 View Your Graph

Open in browser:

https://pixe.la/v1/users/YOUR_USERNAME/graphs/graph1.html
🎯 What This Project Demonstrates

REST API integration

POST, PUT, DELETE operations

JSON handling

Authentication via headers

Dynamic date formatting

📅 Progress

Day 37 / 100 Completed ✅

🔐 Security Note

Never upload your real API token to GitHub.
Use placeholder values before pushing your code.
