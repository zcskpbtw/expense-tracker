from database import *
from datetime import date,datetime


def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        return False
    return True

def add_expense_flow():
    d = add_date()
    if d is False:
        return
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
        if amount <= 0:
            print('трата должна быть больше 0')
            continue
        add_expense(d,category,amount)

def add_date():
    track_date = input('\n по умолчанию стоит сегодняшняя дата. поменять? (да / нет) -> ')
    if track_date.lower() == 'да':
            d = input('введите в формате YYYY-MM-DD: ')
            if not is_valid_date(d):
                print('неверный формат!')
                return False
    elif track_date.lower() == 'нет':
        d = date.today().strftime("%Y-%m-%d")
    else:
        print('неизвестная команда')
        return False
    return d

def show_stats():
    if not get_max_category():
        print('\n нет данных \n')
        return

    while True:
        try:
            menu = int(input(" 1.Траты за весь период \n 2.Сумма всех трат за период \n 3.Максимум трат \n 4.Максимальные траты за день \n 5.Среднее за период в день \n 6.Выход \n --> "))
        except ValueError:
            print('выбор должен быть числом! \n ')
            continue

        match menu:
            case 1:
                all_exp = get_all_expenses()
                for id, d, category, amount in all_exp:
                    print(f'{id}. {d}  {category} - {amount}')
                try:
                    line = int(input('\n 1.Удалить трату \n 2.Вернуться \n ->'))
                except ValueError:
                    print('ввод должен быть числом!')
                    continue
                if line == 1:
                    try:
                        id = int(input('Какую трату удалить?(id): '))
                    except ValueError:
                        print('ввод должен быть числом!')
                        continue
                    is_deleted = delete_expense(id)
                    if is_deleted == 1:
                        print('удалено успешно!')
                    elif is_deleted == 0:
                        print('нет траты с таким айди!')
                elif line == 2:
                    continue
                else:
                    print('нет такой команды')
            case 2:
                print(total_expense(), '\n')
            case 3:
                category, amount = get_max_category()
                print(f'{category} - {amount}')
            case 4:
                d, amount = get_max_amounts()
                print(f'{d} : {amount}')
            case 5:
                per_1 = input('введите первый период(YYYY-MM-DD): ')
                per_2 = input('введите второй период(YYYY-MM-DD): ')
                if not is_valid_date(per_1) or not is_valid_date(per_2):
                    print('неверный формат!')
                    continue
                if per_1 > per_2:
                    per_1, per_2 = per_2, per_1
                total, days = get_avg_per_day(per_1, per_2)
                if days == 0:
                    print('Нет такого периода')
                    continue
                elif days > 0:
                    print('Ср. траты в день за этот период составили')
                    print(f'--> {total / days}')
            case 6:
                return
            case _:
                print('введен неверный формат!')
                continue

def show_menu():
    while True:
        try:
            menu = int(input(" 1.Добавить трату \n 2.Статистика \n 3.Очистить все траты \n 4.Очистить период трат \n 5.Выход \n --> "))
        except ValueError:
            print('выбор должен быть числом! \n ')
            continue


        match menu:
            case 1:
                add_expense_flow()
            case 2:
                show_stats()
            case 3:
                line = input('вы действительно хотите удалить все траты?(да / нет) --> ')
                if line.lower() == 'да':
                    res = clean_all()
                    if res > 0:
                        print('траты успешно очищены!')
                    elif res == 0:
                        print('таблица пуста')
                        continue
                else:
                    print('отмена текущего действия')
                    continue
            case 4:
                per_1 = input('введите первый период(YYYY-MM-DD): ')
                per_2 = input('введите второй период(YYYY-MM-DD): ')
                if not is_valid_date(per_1) or not is_valid_date(per_2):
                    print('неверный формат!')
                    continue
                if per_1 > per_2:
                    per_1,per_2 = per_2,per_1
                line_deleted = input('вы действительно хотите удалить период трат?(да / нет) --> ')
                if line_deleted.lower() == 'да':
                    res = delete_expense_per(per_1,per_2)
                    if res > 0:
                        print('траты успешно очищены!')
                    elif res == 0:
                        print('Нет такого периода')
                        continue
                else:
                    print('отмена текущего действия')
                    continue
            case 5:
                break
            case _:
                print('введен неверный формат!')
                continue

def main():
    init_db()
    show_menu()

if __name__ == "__main__":
    main()