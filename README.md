# 🚀 Automated Data Pipeline and Dashboard using Flask

This project builds a complete end-to-end data pipeline and dashboard system using Python. It fetches **real-time astronaut data** from a public API, cleans and stores it, creates insightful charts, and serves both an API and a dashboard using Flask.

---

## 📌 Project Overview

| Feature | Description |
|--------|-------------|
| 🛰️ Data Source | [Open Notify Astronaut API](http://api.open-notify.org/astros.json) |
| 🧹 Data Cleaning | Column name cleanup, timestamps, and enriched details |
| 🗃️ Storage | SQLite database (via SQLAlchemy) |
| 🔁 Pipeline | Automated script to fetch, clean, and store data |
| 📊 Visualizations | Bar and pie charts using `matplotlib` |
| 🌐 Web App | Flask app with REST API + HTML dashboard |
| ✅ Testing | Pytest for route & data validation (coming soon) |
| 🧠 Built with | Python, Pandas, Flask, SQLAlchemy, Matplotlib |

---

## 📂 Project Structure

Automated_Data_pipeline_flask/
│
├── app.py # Main Flask app
├── .gitignore
├── README.md
├── requirements.txt
├── astronauts_data.db # SQLite database
├── Automated Data Pipeline.ipynb
├── Automated Data Pipeline2.ipynb
│
├── static/ # Chart images
│ ├── astronauts_chart.png
│ ├── pie_chart.png
│ └── ...
│
├── templates/
│ └── dashboard.html # HTML page with table and charts
│
└── tests/
└── test_app.py # Pytest test cases


## ⚙️ How to Run the Project

### 1. Clone the repository

git clone https://github.com/github-anushree/automated-data-pipeline.git
cd automated-data-pipeline
2. Install dependencies

pip install -r requirements.txt
3. Start the Flask server

python app.py
Open your browser and visit:


http://127.0.0.1:5000/dashboard
🔗 API Endpoints
Method	Route	Description
GET	/	Welcome message
GET	/api/astronauts	Returns astronaut data in JSON
GET	/dashboard	Loads web dashboard with data and charts

📊 Sample Charts


More charts are loaded dynamically from /static folder.

✅ What’s Next
 Add unit tests using pytest

 Add cron/schedule for auto-refreshing data

 Optional: Deploy using Render or Railway

 Optional: Use PostgreSQL instead of SQLite

 ## 🧾 Sample API Response

Here's an example response from `/api/astronauts`:

![API Response](static/api_response_sample.png)


🙋‍♀️ Author
Anushree Kashyap
📍 Data Analyst & Python Enthusiast
🔗[LinkedIn Profile](https://www.linkedin.com/in/anushreekashyap/)



⭐️ Show Your Support
If you like this project, consider giving it a ⭐ on GitHub and sharing with others who want to learn Python, Flask, or Data Engineering.
