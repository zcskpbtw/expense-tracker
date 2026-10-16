from database import *
from datetime import date

def add_expense_flow():
    d = add_date()
    print('Для выхода из программы напишите выйти')
    while True:
        line = input('Введите трату: ')
        if line.lower() == 'выйти':
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
        add_expense(d,category,amount)


def add_date():
    track_date = input('\n по умолчанию стоит сегодняшняя дата. поменять? (да / нет) -> ')
    if track_date.lower() == 'да':
        d = input('введите в формате YY-MM-DD: ')
    else:
        d = date.today().strftime("%Y-%m-%d")
    return d


def show_stats():
    # if not get_max_category():
    #     print('\n нет данных \n')
    #     return

    while True:
        try:
            menu = int(input(" 1.Траты за весь период \n 2.Сумма всех трат за период \n 3.Максимум трат \n 4.Максимальные траты за день \n 5.Выход \n --> "))
        except ValueError:
            print('выбор должен быть числом! \n ')
            continue

        match menu:
            case 1:
                all_exp = get_all_expenses()
                for d, category, amount in all_exp:
                    print(f'{d}  {category} - {amount}')
            case 2:
                print(total_expense(), '\n')
            case 3:
                max_category = get_max_category()
                for category, amount in max_category:
                    print(f'{category} - {amount}')
            case 4:
                max_amounts = get_max_amounts()
                for d, amount in max_amounts:
                    print(f'{d} : {amount}')
            case 5:
                return
            case _:
                print('введен неверный формат!')
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
                print('введен неверный формат!')
                continue


def main():
    init_db()
    show_menu()

if __name__ == "__main__":
    main()