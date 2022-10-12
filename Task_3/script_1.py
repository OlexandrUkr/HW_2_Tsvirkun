inp = input("Введіть два числа і один з математичних операторів +, -, *, / між ними: ")
while True:
    try:
        res = f"Результат виконання дії дорівнює: {eval(inp)}"
        break
    except ZeroDivisionError:
        res = "Є така думка, що на 0 ділити не можна, вибачте."
        break
    except SyntaxError:
        res = "Математичний оператор має бути між числами."
    except NameError:
        res = "Десь Ви ввели не число, мало бути схоже на приклад: 2+2."
print(res)
