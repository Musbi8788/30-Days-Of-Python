
# Variables in Python

first_name = 'Musbi'
last_name = 'Jawo'
country = 'Gambia'
city = 'Sukuta'
age = 20
is_married = False
skills = ['HTML', 'CSS', 'Bootsrap', 'WordPress', 'Python']
person_info = {
    'firstname':'Musbi', 
    'lastname':'Jawo', 
    'country':'Gambia',
    'city':'Sukuta'
    }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = 'Musbi', 'Jawo', 'Gambia', 20, False

print(first_name, last_name, country, age, is_married)
print('First Name:', first_name)
print('Last Name:', last_name)
print('Country:', country)
print('Age:', age)
print('Is Married:', is_married)