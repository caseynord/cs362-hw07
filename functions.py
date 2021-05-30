# cs362 - hw07
# casey nord
# spring 2021


def fizzbuzz(_input):
    # check type
    if not isinstance(_input, int):
        raise TypeError

    # input should be between 1 and 100
    if _input < 1 or _input > 100:
        raise ValueError

    # print fizzbuzz
    if _input % 3 == 0 and _input % 5 == 0:
        print("FizzBuzz")
    elif _input % 3 == 0:
        print("Fizz")
    elif _input % 5 == 0:
        print("Buzz")
    else:
        print(_input)

def leapyear(_year):
    retVal = False

    if _year % 4 == 0:
        retVal = True
        
    return retVal
