def task4_1():
    pizza = ["dodo", "pepperoni", "meat"]

    for namePizza in pizza:
        print("I like " + namePizza + " pizza!")
    print("I really love pizza!")

def task4_3():
    for i in range(1, 21):
        print(i)

def task4_4():
    listNumber = list(range(1, 1000001))


def task4_5():
    listNumber = list(range(1, 1000001))

    print(min(listNumber))
    print(max(listNumber))
    print(sum(listNumber))


def task4_6():
    numbers = list(range(1, 21, 2))
    for number in numbers:
        print(number)

def task4_7():
    # Генераторы списков
    numbers = [number for number in range(3, 31, 3)]
    print(numbers)

def task4_8():
    # Генераторы списков
    numbers = [number**3 for number in range(1, 11)]
    print(numbers)

def task4_10():
    string = ["The ", "first ", "three ", "items ", "in", "the", "list", "are:"]
    srezThree = string[0:3]
    srezCenter = string[3:6]
    srezEnd = string[-3:]
    print(srezEnd)

def task4_11():
    pizza = ["dodo", "pepperoni", "meat"]
    friend_pizza = pizza[:]

    pizza.append("gavayi")
    friend_pizza.append("margarita")
    print("Моя любимая пицца: ")
    for word in pizza:
        print(word)

    print("Любимая пицца друзей: ")
    for word in friend_pizza:
        print(word)



task4_11()