def calculator(first_number, second_number, operation):
    """This function implements the simplest calculator.
    It supports addition, subtraction, multiplication and division operations."""

    if operation == "+":
        return first_number + second_number

    if operation == "-":
        return first_number - second_number

    if operation == "*":
        return first_number * second_number

    if operation == "/":
        if second_number == 0:
            raise ZeroDivisionError
        return first_number / second_number

    raise ValueError


def main():
    '''The main body of the program.
    Implements receiving data from the user,
    calling the function "calculator" and displaying the results.'''

    while True:

        try:
            first_number = float(input("Введите первое число: "))
            second_number = float(input("Введите второе число: "))
            operation = input("Введите символ операции: ").strip()
            print(calculator(first_number, second_number, operation))
        except ValueError:
            print("Ошибка! Неверный формат введённых данных. Попробуйте снова!")
        except ZeroDivisionError:
            print("Деление на ноль невозможно!")

        print(
            'Если Вы хотите начать сначала, нажмите "Enter",'
            'иначе введите любую последовательность символов для того, чтобы завершить программу.'
        )

        if len(input()) != 0:
            break


if __name__ == "__main__":
    main()
