numb = int(input("Введите число от 1 до 20: "))
percent = str("Процент")
if numb == 1:
    print(str(numb), percent, sep=' ')
elif 1 < numb <= 4:
    print(str(numb), percent + "a", sep=' ')
else:
    print(str(numb), percent + "ов", sep=' ')
