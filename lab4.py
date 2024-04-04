def Zadacha_1():
    num = int(input("Введите число: "))
    if num % 3 == 0:
        print(f"Число {num} делится на три!")
    else:
        print(f"Число {num} не делится на три!")


def Zadacha_2():
    try:
        num = int(input("Введите число: "))
        result = 100 / num
        print(f"Результат деления 100 на {num} равен {result}")
    except ValueError:
        print("Ошибка: Введено некорректное значение. Пожалуйста, введите число.")
    except ZeroDivisionError:
        print("Ошибка: Деление на ноль невозможно.")
    except Exception as e:
        print(f"Ошибка: {e}")


def Zadacha_3():
    day = int(input("Введите день: "))
    month = int(input("Введите месяц: "))
    year = input("Введите год: ")
    a = int(year[-2:])
    if day * month == a:
        print("Дата является магической.")
    else:
        print("Дата не является магической")


def Zadacha_4():
    n = input("Введите номер билета: ")
    s1 = int(n[0]) + int(n[1]) + int(n[2])
    s2 = int(n[3]) + int(n[4]) + int(n[5])
    if s1 == s2:
        print('Билет счастливый')
    else:
        print('Билет не является счастливым')
