import sqlite3

conn = sqlite3.connect('credits.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Client (
               id INTEGER PRIMARY KEY,
               client_name TEXT,
               bank_employee_name TEXT,
               credit_term INTEGER,
               credit_percent REAL,
               credit_amount REAL
               )""")

conn.commit()

def insert_client(client_name, bank_employee_name, credit_term, credit_percent, credit_amount):
    cursor.execute("INSERT INTO Client (client_name, bank_employee_name, credit_term, credit_percent, credit_amount) VALUES (?, ?, ?, ?, ?)", (client_name, bank_employee_name, credit_term, credit_percent, credit_amount))
    conn.commit()
def find_client_by_name(client_name):
    cursor.execute("SELECT * FROM Client WHERE client_name=?", (client_name,))
    return cursor.fetchall()

def find_client_by_amount(credit_amount):
    cursor.execute("SELECT * FROM Client WHERE credit_amount=?", (credit_amount,))
    return cursor.fetchall()

def find_client_by_term(credit_term):
    cursor.execute("SELECT * FROM Client WHERE credit_term=?", (credit_term,))
    return cursor.fetchall()

def delete_client_by_name(client_name):
    cursor.execute("DELETE FROM Client WHERE client_name=?", (client_name,))
    conn.commit()

def delete_client_by_employee(bank_employee_name):
    cursor.execute("DELETE FROM Client WHERE bank_employee_name=?", (bank_employee_name,))
    conn.commit()

def delete_client_by_term(credit_term):
    cursor.execute("DELETE FROM Client WHERE credit_term=?", (credit_term,))
    conn.commit()

def edit_client_credit_amount(client_name, new_credit_amount):
    cursor.execute("UPDATE Client SET credit_amount=? WHERE client_name=?", (new_credit_amount, client_name))
    conn.commit()
insert_client("Иванов Иван Иванович", "Петров Петр Петрович", 12, 10.5, 50000.0)

