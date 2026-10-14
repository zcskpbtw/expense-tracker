from database import *

def add_expense_flow():
    print('Для выхода из программы напишите exit')
    while True:
        line = input('Введите трату: ')
        if line.lower() == 'exit':
            break
        category, amount = line.split()
        add_expense(category,amount)


def show_stats():
    while True:
        menu = int(input(" 1.Траты за весь период \n 2.Сумма всех трат за период \n 3.Максимум трат \n 4.Выход \n --> "))

        match menu:
            case 1:
                print(get_all_expense(),'\n')
            case 2:
                print(total_expense(), '\n')
            case 3:
                print(get_max_category(), '\n')
            case 4:
                return


def show_menu():
    while True:
        menu = int(input(" 1.Добавить трату \n 2.Статистика \n 3.Выход \n --> "))

        match menu:
            case 1:
                add_expense_flow()
            case 2:
                show_stats()
            case 3:
                exit()



def main():
    show_menu()


main()