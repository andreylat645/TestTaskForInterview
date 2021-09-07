def task6_1():
    men1 = {"first_name": "Вячеслав", "last_name": "Зайко", "age": "23", "city": "Рязань"}
    print(men1["first_name"])
    print(men1["last_name"])
    print(men1["age"])
    print(men1["city"])


def task6_2():
    likeNumbers = {"Лена": "2", "Слава": "8", "Никита": "3"}
    print(likeNumbers["Лена"])
    print(likeNumbers["Слава"])
    print(likeNumbers["Никита"])


def task6_4():
    definition = {"Программа": "Данные и алгоритм", "Цикл": "Перебор данных", "Условие": "Выбор действия по уловию"}
    for key, value in definition.items():
        print("\nОпределение: " + key + " - " + value)


def task6_5():
    river_country = {"nile": "egypt", "lena": "russia", "temza": "england"}
    for river, country in river_country.items():
        print("The " + river.title() + " runs through " + country.title())
    for river in river_country.keys():
        print("River: " + river.title())
    for country in river_country.values():
        print("Country " + country.title())


def task6_6():
    peopleUnsolicited = ["sarah", "andrey"]
    favorite_languages = {
        'jen': 'python',
        'sarah': 'c',
        'edward': 'ruby',
        'phil': 'python',
    }
    for men in peopleUnsolicited:
        if men in favorite_languages.keys():
            print("Thank you, " + men.title())
        else:
            print("Please take a survey, " + men.title())


def task6_7():
    person1 = {"Имя": "Вячеслав", "Фамилия": "Зайко", "Возраст": "23"}
    person2 = {"Имя": "Никита", "Фамилия": "Сбоев", "Возраст": "22"}
    person3 = {"Имя": "Мария", "Фамилия": "Макарова", "Возраст": "20"}

    people = [person1, person2, person3]
    for man in people:
        for key, value in man.items():
            print("Info: " + key + ": " + value)


def task6_8():
    murka = {"Вид животного": "парнокопытный", "Владелец": "Татьяна Ивановна"}
    petka = {"Вид животного": "кошка", "Владелец": "Иван Петрович"}

    pets = [murka, petka]
    for pet in pets:
        for key, value in pet.items():
            print("Info: " + key + ": " + value)

def task6_9():
    favorite_places = {"Кремль": ["Татьяна", "Альберт"],
                       "Некоторое царство": ["Настя", "Андрей", "Егор"],
                       "Памятник": ["Галина", "Валерий"]
                       }

    for place, names in favorite_places.items():
        print("\nЛюбимая достопремечательность: " + place.title())
        for name in names:
            print("\t" + name)

def task6_10():
    cities = {"moscow": {"country": "russia", "population": "15 000 000"},
              "ryazan": {"country": "russia", "population": "1 000 000"},
              "kazan": {"country": "russia", "population": "5 000 000"}
              }

    for city, info in cities.items():
        print("\nГород: " + city.title())
        country = info["country"]
        popul = info["population"]
        print("\n\tСтрана: " + country.title() + "\n\tНаселение: " + popul)



task6_10()
