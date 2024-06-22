from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Список товаров на складе (для примера, в памяти)
inventory = [
    {'name': 'Кокосик', 'description': 'Песочное печенье с кокосом', 'weight': 0.3, 'quantity': 545, 'price': 35.0},
    {'name': 'Медведи', 'description': 'Фигурный жевательный мармелад', 'weight': 0.05, 'quantity': 1500, 'price': 33.0},
    {'name': 'Чебурашка', 'description': 'Прохладительный напиток со вкусом апельсина', 'weight': 1.5, 'quantity': 650, 'price': 45.0},
]

@app.route('/')
def index():
    return render_template('Task#4.html', inventory=inventory)

@app.route('/add', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        # Получаем данные из формы
        name = request.form['name']
        description = request.form['description']
        weight = float(request.form['weight'])
        quantity = int(request.form['quantity'])
        price = float(request.form['price'])

        # Добавляем новый товар в список
        new_item = {
            'name': name,
            'description': description,
            'weight': weight,
            'quantity': quantity,
            'price': price
        }
        inventory.append(new_item)

        # Перенаправляем на главную страницу
        return redirect(url_for('index'))
    return render_template('Task#4.1.html')

if __name__ == '__main__':
    app.run(debug=True)
