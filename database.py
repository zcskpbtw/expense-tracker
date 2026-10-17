import sqlite3


def init_db():
    con_expenses = sqlite3.connect('expenses.db')
    cur_exp = con_expenses.cursor()
    cur_exp.execute('CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY AUTOINCREMENT, date, category, amount INT);')
    con_expenses.commit()
    con_expenses.close()


def add_expense(date, category, amount):
    con_expenses = sqlite3.connect('expenses.db')
    cur_exp = con_expenses.cursor()
    cur_exp.execute('INSERT INTO expenses (date, category, amount) VALUES (?,?,?);', (date,category,amount))
    con_expenses.commit()
    con_expenses.close()


def get_all_expenses():
    con_expenses = sqlite3.connect('expenses.db')
    cur_exp = con_expenses.cursor()
    cur_exp.execute('SELECT id, date, category, amount FROM expenses ORDER BY date ASC;')
    all_exp = cur_exp.fetchall()
    con_expenses.close()
    return all_exp


def total_expense():
    con_expenses = sqlite3.connect('expenses.db')
    cur_exp = con_expenses.cursor()
    cur_exp.execute('SELECT SUM(amount) FROM expenses;')
    total_exp = cur_exp.fetchone()[0]
    con_expenses.close()
    return total_exp


def get_max_category():
    con_expenses = sqlite3.connect('expenses.db')
    cur_exp = con_expenses.cursor()
    cur_exp.execute('SELECT category, SUM(amount) FROM expenses GROUP BY category ORDER BY SUM(amount) DESC LIMIT 1 ;')
    max_summ_category = cur_exp.fetchall()
    con_expenses.close()
    return max_summ_category


def get_max_amounts():
    con_expenses = sqlite3.connect('expenses.db')
    cur_exp = con_expenses.cursor()
    cur_exp.execute('SELECT date, SUM(amount) FROM expenses GROUP BY date ORDER BY SUM(amount) DESC LIMIT 1 ;')
    max_summ_amounts = cur_exp.fetchall()
    con_expenses.close()
    return max_summ_amounts


# def get_avg_per_day():
#     con_expenses = sqlite3.connect('expenses.db')
#     cur_exp = con_expenses.cursor()
#     cur_exp.execute('SELECT category,amount FROM expenses;')
#     cur_exp.fetchall()
#     con_expenses.close()


def delete_expense(id):
    con_expenses = sqlite3.connect('expenses.db')
    cur_exp = con_expenses.cursor()
    cur_exp.execute('DELETE FROM expenses WHERE id=?',(id,))
    con_expenses.commit()
    result = cur_exp.rowcount
    con_expenses.close()
    return result

def clean_all():
    con_expenses = sqlite3.connect('expenses.db')
    cur_exp = con_expenses.cursor()
    cur_exp.execute('DELETE FROM expenses')
    con_expenses.commit()
    result = cur_exp.rowcount
    con_expenses.close()
    return result


