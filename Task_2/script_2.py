inp = input("Введіть число: ")
while True:
    try:
        n = int(inp)
        list_1 = list()
        for i in range(n):
            list_1.append(i ** 3)
        print(list_1)
        qu = input("Створити такий самий список з використанням генератору списків? y/n: ")
        if qu == "y":
            list_2 = [i ** 3 for i in range(n)]
            print(list_2)
        elif qu == "n":
            pass
        else:
            print("Бачу Ви самі не визначились, тому виконання программи припиняється.")
        break
    except ValueError:
        print("Программа очікує ціле число.")
        break
