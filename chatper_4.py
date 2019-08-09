#1
def squared(x):
    """
    Returns x squared
    :param x: int.
    """
    return x ** 2 

#2
def printString(randomString):
    """
    Prints string
    :param randomString: str.
    """
    print(randomString)

#3
def threeRequiredTwoOptional(x, y, z, a=1, b=2):
    """
    Returns sum of parameters
    :param x: int.
    :param y: int.
    :param z: int.
    :param a: int.
    :param b: int.
    """
    return x + y + z + a + b

#4
def divide(x, y):
    """
    Returns x / y
    :param x: int.
    :param y: int.
    """
    return x / y

def multiplyByFour(x):
    """
    Returns x * 4
    :param x: int.
    """
    return x * 4

x = divide(8, 2)
y = multiplyByFour(x)

#5
def stringToFloat(stringFloat):
    """
    Returns float
    :param stringFloat: str.
    """
    try:
        float(stringFloat)
    except ValueError:
        print("Invalid input")
    return floatFromString
    