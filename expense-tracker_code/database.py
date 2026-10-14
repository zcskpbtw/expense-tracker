import sqlite3


def init_db():
    con_expenses = sqlite3.connect('expenses.db')
    cur_exp = con_expenses.cursor()
    cur_exp.execute('CREATE TABLE IF NOT EXISTS expenses (category, amount INT);')
    con_expenses.commit()
    con_expenses.close()


def add_expense(category, amount):
    con_expenses = sqlite3.connect('expenses.db')
    cur_exp = con_expenses.cursor()
    cur_exp.execute('INSERT INTO expenses (category, amount) VALUES (?,?);', (category,amount))
    con_expenses.commit()
    con_expenses.close()


def get_all_expense():
    con_expenses = sqlite3.connect('expenses.db')
    cur_exp = con_expenses.cursor()
    cur_exp.execute('SELECT category, amount FROM expenses;')
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


# def get_avg_per_day():
#     con_expenses = sqlite3.connect('expenses.db')
#     cur_exp = con_expenses.cursor()
#     cur_exp.execute('SELECT category,amount FROM expenses;')
#     cur_exp.fetchall()
#     con_expenses.close()


def clean():
    con_expenses = sqlite3.connect('expenses.db')
    cur_exp = con_expenses.cursor()
    cur_exp.execute('DELETE FROM expenses')
    con_expenses.commit()
    con_expenses.close()


clean()
