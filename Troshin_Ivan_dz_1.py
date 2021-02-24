#Задание № 1
duration = int(input("Введите значение в секундах: "))
second = duration % 60
minutes = (duration // 60) % 60
hour = (duration // 3600) % 24
day = (duration // 86400)
if duration < 60:
    print(str(second) + "сек")
elif 60 < duration < 3600:
    d_minutes = (str(minutes) + "мин" + ':' + str(second) + "сек")
    print(d_minutes)
elif 3600 < duration < 86400:
    d_hour = (str(hour) + "час" + ':' + str(minutes) + "мин" + ':' + str(second) + "сек")
    print(d_hour)
else:
    str(day > duration)
print(str(day) + "дн" + ':' + (str(hour) + "час" + ':' + str(minutes) + "мин" + ':' + str(second) + "сек"))