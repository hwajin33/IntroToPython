# Can put different values into a list
First_List = ["Kevin", 2, False]

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
print(friends[2])

# accessing from the back of the list
print((friends[-2]))

# accessing from position 1 and all the others after that
print((friends[1:]))

# accessing all the elements from position 1 but not including the 3rd one
print((friends[1:3]))

# modifying element in the list
friends[1] = "Mike"
print(friends[1])
