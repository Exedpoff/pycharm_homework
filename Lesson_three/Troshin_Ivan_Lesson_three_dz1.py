num = input("Введите число на Англиском: ")
numirate = {"zero": "ноль", "one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
            "six": "шесть",
            "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"
            }


def translate_num(word):
    return numirate.get(word)


print(translate_num(num))
