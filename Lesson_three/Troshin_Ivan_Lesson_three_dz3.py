def thesaurus(*name):
    name_dir = {}
    for i in sorted(name):
        key = i[0]
        if key in name_dir:
            name_dir[key] += [i]
        else:
            name_dir[key] = [i]
    return name_dir


name_diction = thesaurus("Иван", "Мария", "Михаил", "Илья", "Алина", "Николай", "Никита")
print(name_diction)
