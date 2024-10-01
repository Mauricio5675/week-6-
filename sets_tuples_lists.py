# #collection = single "variables" used to store multiple values
# # List = [] ordered and changeable. Duplicates OK
# # Set = {} unordered and immutable, but Add/ Remove Ok. No duplicates.
# # Tiple = () ordered and unchangable. Duplicates Ok. FASTER

# # fruits = ["apple","orange","banana","coconut"]
# # print(dir(fruits))
# # print(help(fruits)) #prints helps
# # print(len(fruits)) # prints the amount of words in your list
# # print("pineapple" in fruits ) #prints true or false if a word is in the list (boolean)
# # fruits.add("pineapple")
# # fruits.remove("apple")
# # fruits.pop() #Pops it off 
# # fruits.clear()

# # "apple in fruits"
# # for fruit in fruits:
# # print(fruit)  (prints the list from top to bottom)

# # fruits[0] = "pineapple" # changeing apple to pineapple (reassigns words in list)
# # fruits.append("pineapple")
# # fruits.remove("apple") #removes word from list
# # fruits.insert(0,"pineapple") #adds values in list
# # fruits.sort() #sorts the list
# # fruits.reverse() #reverses the list
# # fruits.clear()

# #looping throught the list
# # #otherwise called iterating throught the list
# # cars = ["Chevy", "Mercedes", "GMC", "Ford"]
# # for car in cars:
# # # print(len(car)

# # fruits = ("apple","orange","banana","coconut, coconut")
# # print(dir(fruits))
# # # print(help(fruits)) #prints helps
# # # print(len(fruits)) # prints the amount of words in your list
# # print("pineapple" in fruits ) #prints true or false if a word is in the list (boolean)
# # print(fruits.index("apple"))
# # print(fruits.count("coconut"))

# # print(fruits)
# # for fruit in fruits:
# #     print(fruit)

# # fruits.add("pineapple")
# # fruits.remove("apple")
# # fruits.pop() #Pops it off 
# # fruits.clear()




# # dictionary = a Collection of {key : value} pairs
# #              ordered and changeable. No duplicates

# capitals = {"USA": "Washington D.C",
#             "India": "New Delhi",
#             "China": "Beijing",
#             "Russia": "Moscow"}
# # print(dir(capitals))
# # print(help(capitals))
# print(capitals.get("Japan"))
# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")
# print(capitals.get("Russia"))
# capitals.update({"Mexico": "Mexico City"})
# capitals.update({"Germany": "Berlin"})
# capitals.pop("China")
# capitals.popitem
# capitals.clear()

# keys = capitals.keys()

# for key in capitals.keys() :
#     print(key)

# values = capitals.values()
# for value in capitals.values():
#     print(value)

# items = capitals.items()
# for key, value in capitals.items():
#     print(f"{key}: {value}")
