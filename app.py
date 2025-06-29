import os
from flask import Flask, jsonify, render_template, url_for
import pandas as pd
from sqlalchemy import create_engine

app = Flask(__name__)
engine = create_engine("sqlite:///astronauts_data.db")

@app.route("/")
def home():
    return "Astronauts API is running!"

@app.route("/api/astronauts", methods=["GET"])
def get_astronauts():
    df = pd.read_sql("SELECT * FROM astronauts", con=engine)
    data = df.to_dict(orient="records")
    return jsonify(data)

@app.route("/dashboard")
def dashboard():
    df = pd.read_sql("SELECT * FROM astronauts", con=engine)
    columns = df.columns.tolist()
    rows = df.values.tolist()

    # ✅ Get all .png chart files from /static
    chart_folder = os.path.join(app.static_folder)
    chart_files = [f for f in os.listdir(chart_folder) if f.endswith('.png')]

    return render_template("dashboard.html", columns=columns, rows=rows, chart_files=chart_files)

# 🔥 This part was missing!
if __name__ == "__main__":
    print(">>> Flask server is starting...")
    app.run(debug=True)
