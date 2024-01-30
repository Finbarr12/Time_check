from flask import Flask
from datetime import datetime


app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this page"

@app.route("/getTime")
def grret_time():
    current_time = datetime.now().time().hour
    
    if current_time < 12:
        return "Good morning user✋. The time is "f"{datetime.now().strftime("%I:%M %p")}"
    elif current_time > 12 and current_time <= 15:
        return "Good Afternoon user✋. The time is "f"{datetime.now().strftime("%I:%M %p")}"
    elif current_time > 15 and current_time <= 19:
        return "Good evening user✋. The time is "f"{datetime.now().strftime("%I:%M %p")}"
    else:
        return "Good night user✋. The time is "f"{datetime.now().strftime("%I:%M %p")}"


if __name__ == "__main__":
    app.run(debug=True)