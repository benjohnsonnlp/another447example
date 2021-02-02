def hi(message, count):
    print(message)
    number_of_cars, y = meaningless_math()

    print(number_of_cars, y)


def meaningless_math():
    number_of_cars = 5
    y = number_of_cars + 3
    return number_of_cars, y


if __name__ == '__main__':
    hi("yo", 5)
    print("Hey.  Is this scary?  Maybe at first.  But we IDEs want to help!")
