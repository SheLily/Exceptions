expr = input('Выражение: ').split(' ')

try:

    assert expr[0] in ('+', '-', '/', '*')

    if expr[0] == '+':
        value = float(expr[1]) + float(expr[2])
    elif expr[0] == '-':
        value = float(expr[1]) - float(expr[2])
    elif expr[0] == '*':
        value = float(expr[1]) * float(expr[2])
    elif expr[0] == '/':
        value = float(expr[1]) / float(expr[2])

    print(value)

except AssertionError:
    print(f'Недопустимая операция {expr[0]}')

except ZeroDivisionError:
    print('Деление на ноль')

except ValueError:
    print(f'Одно или несколько введенных значений не являются числами')

except IndexError:
    print(f'Требовалось ввести 3 значения, получено {len(expr)}')

except:
    print('Неизвестная ошибка')