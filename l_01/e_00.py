name = None  # input()
age = None  # int(input())
town = None  # input()


def greetings_by_name(name='user', age=0, town='Sofia'):
    read_input()
    print(f'Hello my name is {name} and i {age} old from {town}')


def read_input():
    name = 'Dimitar'  # input()
    age = 28  # int(input())
    town = 'Plovdiv'  # input()


greetings_by_name(name, age, town)
