s = 0
n = 0
while True:
    inp = input("Введіть число, або /q для зупинки: ")
    if inp != "/q":
        try:
            num = float(inp)
            n += 1
            s += num
            continue
        except ValueError:
            print("Тип данних не відповідає умовам, спробуйте ввести ще раз.")
            continue
    else:
        pass
        break
if n != 0:
    print(f"Середнє арифметичне чисел, що було введено: {s/n}")
else:
    print(f"Не було введено жодного числа.")
