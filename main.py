from click import clear
from database import *
from datetime import date

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
        add_expense(d,category,amount)


def add_date():
    track_date = input('\n по умолчанию стоит сегодняшняя дата. поменять? (да / нет) -> ')
    if track_date.lower() == 'да':
        d = input('введите в формате YYYY-MM-DD: ')
        date_split = d.split('-')
        if len(date_split) != 3 or len(date_split[0]) != 4 or len(date_split[1]) != 2 or len(date_split[2]) != 2:
            print('Введен неверный формат. попробуйте еще раз')
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
            menu = int(input(" 1.Траты за весь период \n 2.Сумма всех трат за период \n 3.Максимум трат \n 4.Максимальные траты за день \n 5.Выход \n --> "))
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
            menu = int(input(" 1.Добавить трату \n 2.Статистика \n 3.Очистить все траты \n 4.Выход \n --> "))
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
                    print('отмена текщего действия')
                    continue
            case 4:
                break
            case _:
                print('введен неверный формат!')
                continue


def main():
    init_db()
    show_menu()

if __name__ == "__main__":
    main()