# Creating a tuple
tuple1 = ('item1', 'item2', 'item3')

fruists = ('orange', 'mango', 'adama', 'banana')

# Tuple length
print(len(fruists)) # 4

# Accessing tuples
mango = fruists[1] # mango
print(mango)

last_fruist = fruists[-1] 
print(last_fruist) # banana

adama = fruists[-2]
print(adama)  # adama

# Slicing tuples
fruits = ('orange', 'mango', 'adama', 'banana')
all_fruits = fruits[0:4] # All items
mango_adama = fruits[1:3] 
print(mango_adama) # ('mango','adama')

# changing a tuples to a lists
tuples_to_lists = list(fruits)
print(tuples_to_lists) # ['orange', 'mango', 'adama', 'banana']
print(fruits) # ('orange', 'mango', 'adama', 'banana')

# Checking an item in a tuple

print('adama' in fruits) # True
