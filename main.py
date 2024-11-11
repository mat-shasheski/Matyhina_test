spisok = []
while True:
    a = input("впишите элемент цикла.для завершения введите 0.")
    if a == "0":
        break
    else:
        spisok.append(a)
print(sorted(spisok, reverse=True))