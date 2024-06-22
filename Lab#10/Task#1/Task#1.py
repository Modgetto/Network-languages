from flask import Flask, render_template
from datetime import datetime


app = Flask(__name__)

def get_greeting():
    current_hour = datetime.now().hour
    if 6 <= current_hour < 12:
        return 'Доброе утро'
    elif 12 <= current_hour < 18:
        return 'Добрый день'
    elif 18 <= current_hour < 24:
        return 'Добрый вечер'
    else:
        return 'Доброй ночи'


@app.route('/')
def index():
    greeting = get_greeting()
    return render_template('C:\Users\vladp\Desktop\Lab#10\Task#1\templates\main.html', greeting=greeting)



if __name__ == '__main__':
    app.run(debug=True)