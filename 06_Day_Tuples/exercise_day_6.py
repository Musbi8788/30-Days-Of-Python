# Level 1

from typing import Literal


tuples = ()

sisters = ("Jainaba", "Kaddijatou")
brothers = ("Lax", "Ebrima")

# Joining brothers and sisters
siblings = brothers + sisters
print(len(siblings)) # 4

mother_farther = ("Penda", "Ebrima")

family_member = siblings + mother_farther
print("Family Members are: ", family_member)

# Level 2

fruits: tuple[Literal['mango'], Literal['orange']] = ("mango", "orange", "apple") # type: ignore
vegetables: tuple[Literal['casava'], Literal['banana']] = ("casava", "banana", "rice") # type: ignore
animals: tuple[Literal['goat'], Literal['sheep']] = ("goat", "sheep", "cow") # type: ignore
food_stuff_tp: tuple[Literal['mango'], Literal['orange'], Literal['casava'], Literal['banana'], Literal['goat'], Literal['sheep']] = fruits + vegetables + animals

food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# slicing the middle items
middle_item = food_stuff_lt[4:5] # casava, banana
print(middle_item)

# slice out the first and last three items
first_three_items = food_stuff_lt[:3]
print(first_three_items)
last_three_items = food_stuff_tp[-3:]
print(last_three_items)

# delete tuple
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

if 'The Gambia' in nordic_countries:
    print("Yes") # False

if 'Iceland' in nordic_countries:
    print("Yes Iceland is a nordic country.") # True

print("The Gambia" in nordic_countries) # False
print("Iceland" in nordic_countries) # True