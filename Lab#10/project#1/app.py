from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.now()
    current_hour = now.hour

    if 6 <= current_hour < 12:
        greeting = "Доброе утро"
    elif 12 <= current_hour < 18:
        greeting = "Добрый день"
    elif 18 <= current_hour < 24:
        greeting = "Добрый вечер"
    else:
        greeting = "Доброй ночи"

    return render_template('index.html', greeting=greeting)

if __name__ == '__main__':
    app.run(debug=True)