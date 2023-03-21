def check_digits(value):

    if not value.lstrip("-").replace(",", ".").replace(".", "", 1).isdigit():
        print('Не правильный ввод!')

    elif value.lstrip("-") == "0":
        print("Вы ввели число ноль")

    elif "." in value or "," in value:
        if value[0] == "-":
            print(f"Вы ввели дробное отрицательное число {value}")
        else:
            print(f"Вы ввели дробное положительное число {value}")

    else:
        if value[0] == "-":
            print(f"Вы ввели целое отрицательное число {value}")
        else:
            print(f"Вы ввели целое положительное число {value}")


while True:
    user_input = input("Введите число или или одно из значений: 'выход', 'exit', 'quit', 'e' или 'q': ")
    if user_input.lower() in ['выход', "exit", 'quit', 'e', 'q']:
        break

    else:
        check_digits(user_input)