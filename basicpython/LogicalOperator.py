# age checking


# age = input('Enter your age: ')

# here .split() was creating error because it was expecting another variable value.
# testing condition
# There must be : at the end of condition and at default value i.e.

# age = int(age)
# we can use eval which convert automatically string int
age = eval(input('Entere your age: '))

if (age >= 1) | (age < 18):
    print('your age is {} which is Important'. format(age))

elif (age == 21) | (age == 50) | (age > 65):
    print('your age is {} which is Important'.format(age))

else:
    print('Your age is {} , It is more important'.format(age))
