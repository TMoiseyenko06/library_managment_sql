from connect_database import connect
from mysql.connector import Error

conn = connect()
if conn is not None:
    cursor = conn.cursor()

def add_book(book_name,author_id):
    try:
        cursor.execute('INSERT INTO books (name,author_id,borrowed) VALUES (%s,%s,%s)',(book_name,author_id,0))
        conn.commit()
    except:
        print('An error occured please try again.')
    else:
        print('Book Succsesfully Added')

def add_author(author_name,biography):
    cursor.execute('INSERT INTO authors (name,biography) VALUES (%s,%s)',(author_name,biography))
    conn.commit()

def borrow_book(book_id,user_id):
    try:
        cursor.execute('SELECT * FROM books WHERE id = %s and borrowed = 0',(book_id,))
        results = cursor.fetchall()
        if results == []:
            print('Book either does not exist or is already borrowed by somebody, please try again.')
            return
        cursor.execute('INSERT INTO current_transactions (user_id, book_id) VALUES (%s, %s)', (user_id, book_id))
        cursor.execute('UPDATE books SET borrowed = 1 WHERE id = %s', (book_id,))
        conn.commit()
    except Error as e:
        print(f'A database error has occuered: {e}')

def return_book(book_id,user_id):
    try:
        cursor.execute('SELECT * FROM current_transactions WHERE user_id = %s AND book_id = %s',(user_id,book_id))
        if cursor.fetchall() == []:
            print('This book either does not exist or this user does not currently have it, please try again.')
            return
        cursor.execute('DELETE FROM current_transactions WHERE user_id = %s AND book_id = %s',(user_id,book_id))
        cursor.execute('UPDATE books SET borrowed = 0 WHERE id = %s',(book_id,))
        conn.commit()
    except Error as e:
        print(f'A database error occured: {e} please try again.')

def add_user(user_name):
    cursor.execute('INSERT INTO users (name) VALUES (%s)',(user_name,))
    conn.commit()

def get_user_name(user_id):
    cursor.execute('SELECT name FROM users WHERE id = %s',(user_id,))
    return cursor.fetchone()[0]

def get_book_name(book_id):
    cursor.execute('SELECT name FROM books WHERE id = %s',(book_id,))
    return cursor.fetchone()[0]

def get_author_name(author_id):
    cursor.execute('SELECT name FROM authors WHERE id = %s',(author_id,))
    return cursor.fetchone()[0]

def search_for_book(book_id):
    try:
        cursor.execute('SELECT * FROM books WHERE id = %s',(book_id,))
        result = cursor.fetchone()
        book_name = result[1]
        book_author = get_author_name(result[2])
        book_borrowed = True if result[3] == 1 else False
        print(f'Book with id of {book_id}:\nName: {book_name}\nAuthor: {book_author}\nThis book is {'currently out' if book_borrowed else 'currently avalible'}')
    except TypeError:
        print('This book does not exist, please try again.')
    except Error as e:
        print(f'A database error occured: {e} please try again.')

def display_all_books():
    cursor.execute('SELECT * FROM books')
    results = cursor.fetchall()
    for result in results:
        book_id = result[0]
        book_name = result[1]
        book_author = get_author_name(result[2])
        book_borrowed = True if result[3] == 1 else False
        print(f'Book with id of {book_id}:\nName: {book_name}\nAuthor: {book_author}\nThis book is {'currently out' if book_borrowed else 'currently avalible'}')

def view_user(user_id):
    cursor.execute('SELECT name FROM users WHERE id = %s',(user_id,))
    result = cursor.fetchone()
    cursor.execute('SELECT book_id FROM current_transactions WHERE user_id = %s',(user_id,))
    books = cursor.fetchall()
    print(f'{result[0]}:')
    if books == []:
        print('This user currently has no books out.')
    else:
        print('Here are the books that the user currently has out:')
        for book in books:
            print(f'\n{get_book_name(book[0])}')

def display_all_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    for user in users:
        view_user(user[0])

def view_author(author_id):
    cursor.execute('SELECT * FROM authors WHERE id = %s',(author_id,))
    author = cursor.fetchone()
    print(f'Author: {author[1]}, Biography: {author[2]}')

def display_all_authors():
    cursor.execute('SELECT * FROM authors')
    authors = cursor.fetchall()
    for author in authors:
        view_author(author[0])