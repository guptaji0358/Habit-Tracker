# Habit-Tracker
DAY - 37/100  - Project - python X Habit Tracker via Pixela

# Habit Tracker via Pixela

**DAY – 37 – Project – Python Habit Tracker using Pixela API**

This project is part of the **100 Days of Code – Python Bootcamp** challenge.  
It uses Python and the Pixela REST API to build a simple habit tracker that logs daily entries as pixels on a graph.

* * *

## 🚀 Features

* Create a Pixela user (one-time setup)
* Create a graph to track data (hours / km / habits)
* Update graph properties
* Add daily habit entries (pixels)
* Delete individual pixel entries
* View the graph in browser
* Token-based authentication

* * *

## 🛠 Technologies Used

* Python 3
* `requests` library
* `datetime`
* REST API (Pixela)

* * *

## 📁 Project Structure


37_HABIT_TRACKER_VIA_PIXELA.py
README.md


* * *

## 🔧 How It Works

1. Sign up for a Pixela account programmatically using your custom token and username.
2. Create a graph with ID, name, unit, type, and color.
3. Update graph details like name, unit, or color.
4. Add a pixel for today’s date with your habit data.
5. Optionally delete a pixel entry.
6. View your graph in the browser.

* * *

## ✨ Setup Instructions

### 1️⃣ Install dependencies

```bash
pip install requests
2️⃣ Update script variables

Open 37_HABIT_TRACKER_VIA_PIXELA.py and replace:

My_Piixela_API_Token = "YOUR_API_TOKEN"
My_Pixela_User_Name = "YOUR_USERNAME"
3️⃣ Run the program
python 37_HABIT_TRACKER_VIA_PIXELA.py
📈 Example Usage
Add a daily entry (pixel)
today = datetime.now().strftime("%Y%m%d")

pixel_data = {
    "date": today,
    "quantity": input("Enter Your Total Hours: ")
}
View the graph in your browser
https://pixe.la/v1/users/YOUR_USERNAME/graphs/graph1.html
📅 What You Will Learn

Working with REST APIs

Sending POST, PUT, DELETE requests

Handling JSON payloads

Token authentication headers

Formatting dates for API use

Debugging API responses in Python

📌 Challenge Progress

Day 37 / 100 Completed ✅

⚠️ Important Notes

✔ Do NOT upload your real API token on GitHub
✔ Always use placeholder values before pushing

📄 Author

Robin Gupta
100 Days of Code – Day 37
