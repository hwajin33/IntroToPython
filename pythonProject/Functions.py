
def say_hi(name, age):
    # converting the age element which is an integer to a string element for printing
    print("Hello " + name + " you are, " + str(age))


say_hi("Mike", 35)
say_hi("Steve", 24)


def cube(num):
    return num*num*num


# holding the value that has been executed by cube()
result = cube(4)
print(result)
