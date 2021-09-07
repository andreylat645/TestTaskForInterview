def task3_1():
    names = ["слава", "никита", "андрей", "лиза"]
    print(names[0].title())
    print(names[1].title())
    print(names[2].title())
    print(names[3].title())

def task3_2():
    names = ["слава", "никита", "андрей", "лиза"]
    print(names[0].title() + " лучший друг.")
    print(names[1].title() + " лучший друг.")
    print(names[2].title() + " лучший друг.")
    print(names[3].title() + " лучший друг.")

def task3_4():
    guests = ["мама", "бабушка", "сестра", "жена",]

    for word in guests:
        print(word.title() + ", приглашаю на торжество!")


def task3_5():
    guests = ["мама", "бабушка", "сестра", "жена", ]

    failGuest = guests[1].title()
    print(failGuest + " отказалась.")

    newGuest = "Слава"
    guests[1] = newGuest
    print("Новый приглашенный: " + guests[1])
    for word in guests:
        print(word.title() + ", приглашаю на торжество!")


def task3_6():
    print("Обеденный стол расширился!")

    guests = ["мама", "бабушка", "сестра", "жена", ]
    guests.insert(0, "брат")
    guests.insert(3, "дядя")
    guests.append("тетя")
    for word in guests:
        print(word.title() + ", приглашаю на торжество!")

def task3_7():
    print("Приглашаются только 2 гостя! Простите!")

    guests = ["мама", "бабушка", "сестра", "жена", ]
    guests.insert(0, "брат")
    guests.insert(3, "дядя")
    guests.append("тетя")

    while len(guests) > 2:
        print(guests.pop(0).title() + ", я сожалению, что не получистя пригласить!")

    for word in guests:
        print(word.title() + ", предложение остается в силе!")

    del guests[0]
    del guests[0]


    print(guests)


def task3_8():
    country = ["Швеция", "США", "Канада", "Австралия", "Англия"]
    print(country)
    print(sorted(country))
    print(country)
    print(sorted(country, reverse=True))
    print(country)

    country.reverse()
    print(country)
    country.reverse()
    print(country)

    country.sort()
    print(country)

    country.sort(reverse=True)
    print(country)

def task3_9():
    print("Обеденный стол расширился!")

    guests = ["мама", "бабушка", "сестра", "жена", ]
    guests.insert(0, "брат")
    guests.insert(3, "дядя")
    guests.append("тетя")

    print("Всего мест: " + str(len(guests)))

# task3_1()
# task3_2()
# task3_4()
# task3_5()
task3_9()