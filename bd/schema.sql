CREATE DATABASE dbname;

USE dbname;

-- Создание таблицы book
CREATE TABLE book (
    book_id INT PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    price DECIMAL(10, 2),
    amount INT
);


-- Создание таблицы user
CREATE TABLE user (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);

-- Создание таблицы sale
CREATE TABLE sale (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    book_id INT,
    quantity INT,
    sale_date DATE,
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (book_id) REFERENCES book(book_id)
);

-- вставка данных в таблицу book
INSERT INTO book (book_id, title, author, price, amount) VALUES
(1, 'Мастер и Маргарита', 'Булгаков М.А.', 670.99, 1000),
(2, 'Белая гвардия', 'Булгаков М.А.', 540.50, 1000),
(3, 'Идиот', 'Достоевский Ф.М.', 460.00, 1000),
(4, 'Братья Карамазовы', 'Достоевский Ф.М.', 799.01, 1000),
(5, 'Стихотворения и поэмы', 'Есенин С.А.', 650.00, 1000);

-- Вставка данных в таблицу user
INSERT INTO user (username, email, password) VALUES
('user1', 'user1@example.com', 'password1'),
('user2', 'user2@example.com', 'password2'),
('user3', 'user3@example.com', 'password3');

-- Вставка данных в таблицу sale
INSERT INTO sale (user_id, book_id, quantity, sale_date) VALUES
(1, 1, 1, '2023-07-01'),
(1, 2, 2, '2023-07-02'),
(2, 3, 1, '2023-07-03'),
(3, 4, 1, '2023-07-04'),
(3, 5, 3, '2023-07-05');