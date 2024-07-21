from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Настройки базы данных
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root@localhost/class_new'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Модель пользователя
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

# Модель книги
class Book(db.Model):
    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    amount = db.Column(db.Integer, nullable=False)

# Модель продажи
class Sale(db.Model):
    sale_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.book_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    sale_date = db.Column(db.DateTime, default=datetime.utcnow)

# Маршрут для домашней страницы
@app.route('/')
def index():
    return render_template('index.html')

# Маршрут для страницы входа
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            return redirect(url_for('catalog', user_id=user.user_id))
        else:
            return 'Неверные учетные данные'
    return render_template('login.html')

# Маршрут для каталога книг
@app.route('/catalog/<int:user_id>')
def catalog(user_id):
    books = Book.query.all()
    return render_template('catalog.html', user_id=user_id, books=books)

# Маршрут для обработки покупки книги
@app.route('/purchase/<int:user_id>/<int:book_id>', methods=['POST'])
def purchase(user_id, book_id):
    book = Book.query.get(book_id)
    if book and book.amount > 0:
        sale = Sale(user_id=user_id, book_id=book_id, quantity=1)
        book.amount -= 1
        db.session.add(sale)
        db.session.commit()
        return redirect(url_for('catalog', user_id=user_id))
    else:
        return 'Книга недоступна'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
