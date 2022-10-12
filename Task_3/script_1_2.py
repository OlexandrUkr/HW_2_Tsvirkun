inp_2 = input("Введіть два числа і один з математичних операторів +, -, *, / розділяючи їх пробілами: ")
l_2 = inp_2.split()
oper = ""
try:
    a = float(l_2[0])
    try:
        b = float(l_2[2])
        oper = l_2[1]
    except ValueError:
        try:
            b = float(l_2[1])
            oper = l_2[2]
        except ValueError:
            print("Не вдалось розпізнати друге число.")
except ValueError:
    print("На першому місці має бути введене число.")
if oper == "":
    print("Не задана математична дія.")
elif oper == "+":
    rez = a + b
    print(rez)
elif oper == "-":
    rez = a - b
    print(rez)
elif oper == "*":
    rez = a * b
    print(rez)
elif oper == "/" and b != 0:
    rez = a / b
    print(rez)
elif oper == "/" and b == 0:
    print("Ділити на 0 не можна.")
else:
    print("Не вдалось розпізнати оператор, по умові може бути +, -, *, /.")
