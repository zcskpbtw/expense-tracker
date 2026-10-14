from database import *

def add_expense_flow():
    print('Для выхода из программы напишите exit')
    while True:
        line = input('Введите трату: ')
        if line.lower() == 'exit':
            break
        parts = line.split()
        if len(parts) != 2:
            print('Неверный формат записи! \n Пример: еда 200')
            continue
        category = parts[0]
        try:
            amount = int(parts[1])
        except ValueError:
            print('трата должна быть числом!')
            continue
        add_expense(category,amount)


def show_stats():
    while True:
        try:
            menu = int(input(" 1.Траты за весь период \n 2.Сумма всех трат за период \n 3.Максимум трат \n 4.Выход \n --> "))
        except ValueError:
            print('выбор должен быть числом! \n ')
            continue


        match menu:
            case 1:
                all_exp = get_all_expense()
                for category, amount in all_exp:
                    print(f'{category} - {amount}')
            case 2:
                print(total_expense(), '\n')
            case 3:
                max_category = get_max_category()
                for category, amount in max_category:
                    print(f'{category} - {amount}')
            case 4:
                return
            case _:
                print('введен невеный формат!')
                continue


def show_menu():
    while True:
        try:
            menu = int(input(" 1.Добавить трату \n 2.Статистика \n 3.Выход \n --> "))
        except ValueError:
            print('выбор должен быть числом! \n ')
            continue


        match menu:
            case 1:
                add_expense_flow()
            case 2:
                show_stats()
            case 3:
                break
            case _:
                print('введен невеный формат!')
                continue


def main():
    init_db()
    show_menu()

main()