def task2_3(name):
    name = ' ' + name
    print("Hello" + name + ", would you like to learn some Python today?")


def task2_4(name):
    nameUp = name.upper()
    nameLow = name.lower()
    nameTitle = name.title()

    print("Lower: " + nameLow + "\nUpper: " + nameUp + "\nTitle: " + nameTitle)

def task2_5(name):
    print(name + " как то сказал: 'То, что можно сделать сегодня,\n не оставляй на завтра.'")

def task2_6(name):
    famous_person = name
    message = famous_person  + "как то сказал: 'То, что можно сделать сегодня,\n не оставляй на завтра.'"
    print(message)

def task2_7(name):
    name = '   ' + name + '    \t'
    print(name)
    print(name.rstrip())
    print(name.lstrip())
    print(name.strip())

def task2_8():
    print(5+3)
    print(16-8)
    print(2*4)
    print(16/2)

def task2_9(number):
    loveNumber = number
    print("My lovely number is " + str(loveNumber))

def task2_10():
    #Вывод любимого числа
    task2_9(11)


# task2_3("Eric")
# task2_4("Eric")
# task2_5("Eric")
# task2_6("Eric")
# task2_7("Eric")
# task2_8()
# task2_9(11)
task2_10()