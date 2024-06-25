from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'
db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    weight = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        weight = float(request.form['weight'])
        quantity = int(request.form['quantity'])
        price = float(request.form['price'])
        
        new_product = Product(name=name, description=description, weight=weight, quantity=quantity, price=price)
        db.session.add(new_product)
        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('add_product.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
