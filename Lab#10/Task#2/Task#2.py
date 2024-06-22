from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('main.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            tasks.append(task)
        return redirect(url_for('main'))
    return render_template('add_task.html')



if __name__ == '__main__':
    app.run(debug=True)