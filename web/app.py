from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = mysql.connector.connect(
            host="db",
            user="user",
            password="password",
            database="mydb"
        )
        return "Connected to MySQL Database!"
    except:
        return "Database connection failed."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
