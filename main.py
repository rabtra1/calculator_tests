def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b


def main():
    print("=== Консольный калькулятор ===")
    print("Доступные операции: +  -  *  /")

    try:
        a = float(input("Введите первое число: "))
        op = input("Введите операцию: ")
        b = float(input("Введите второе число: "))

        if op == "+":
            print("Результат:", add(a, b))
        elif op == "-":
            print("Результат:", sub(a, b))
        elif op == "*":
            print("Результат:", mul(a, b))
        elif op == "/":
            print("Результат:", div(a, b))
        else:
            print("Неизвестная операция!")

    except ValueError:
        print("Ошибка: введено не число")
    except ZeroDivisionError as e:
        print("Ошибка:", e)


if __name__ == "__main__":
    main()
