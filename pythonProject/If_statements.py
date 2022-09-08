
is_male = False
is_tall = False

# OR statement
if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither a male or tall")


# AND statement
if is_male and is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither a male or tall")


# Else if
if is_male and is_tall:
    print("You are a male or tall or both")
# whether it's a male and not tall
elif is_male and not is_tall:
    print("You are a short male")
# whether it's not a male but tall
elif not is_male and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and not tall")


# Comparison
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(3, 9, 6))
