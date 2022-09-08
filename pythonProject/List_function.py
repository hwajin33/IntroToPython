
lucky_numbers = [4, 8, 12, 16, 20, 24]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]
coffee = ["cafe latte", "americano", "espresso", "pumpkin spice latte"]

# appending two different lists 
friends.extend(lucky_numbers)
print(friends)

# adding individual elements at the end of the list
friends.append("Creed")
print(friends)

# adding an element in the middle (at position 1)
friends.insert(1, "Creed")
print(friends)

# removing an element
friends.remove("Toby")
print(friends)

# removing the last element in the list
friends.pop()
print(friends)

# whether an element is there or not - giving the index of that element if exist
print(friends.index("Karen"))

# count the number of similar elements in the list
print(friends.count("Jim"))

# sorting the list - ordering the list in alphabetical order, only for the list with same types
coffee.sort()
print(coffee)

# reversing the order
friends.reverse()
print(friends)

# copying a list
friends2 = friends.copy()
print(friends2)

# clearing all the elements in the list
friends.clear()
print(friends)

