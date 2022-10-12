list_1 = ["apple", "orange", 1, None, ["dog", "cat"], "book", "car", True, "False"]
list_2 = list()
for el in list_1:
    if type(el) == str:
        list_2.append(el)
print(list_2)
