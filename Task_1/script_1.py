list_1 = list()
while True:
    inp = input("Введіть число, або /q для зупинки: ")
    if inp != "/q":
        try:
            num = int(inp)
            if num % 2 == 0:
                list_1.append(num)
                continue
        except ValueError:
            print("Тип данних не відповідає умовам, спробуйте ввести коректні.")
            continue
    else:
        pass
        break
print(f"Ви ввели таку кількість парних чисел: {len(list_1)}")
