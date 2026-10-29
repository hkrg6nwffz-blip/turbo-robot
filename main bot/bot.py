from flask import Flask, render_template, request
import sqlite3
import os
def init_db():
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"businesspilot.db")
    connection = sqlite3.connect(db_path)
    connection.execute("""
         CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL
        )
    """)
    columns = connection.execute(
        "PRAGMA table_info(tasks)"
    ).fetchall()
    print("TASKS TABLE STRUCTURE:", columns)
    connection.commit()
    connection.close()
app = Flask (__name__)
init_db()
@app.route("/", methods=["GET", "POST"])
def home():
    task = None
    error = None
    if request.method == "POST":
       task = request.form.get("task", "").strip()
        
       if not task:
           error = "Ввидите название задачи"
           task = None
       else:
        connection = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath(__file__)), "businesspilot.db")
        )                             
        print ("SQL QUERY CHECK: VALUES")
        connection.execute(
            "INSERT INTO tasks (title) VALUES (?)",
               (task,)
        )
        connection.commit()
        connection.close()        
    return render_template("bot.html", task=task, error=error)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)