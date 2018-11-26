# single line comment
'''multple line comment
'''

name = input('Enter yout Name: ')

print('Hello ', name, '!!!')

'''
# ask the user two input and store them on variable and sum and diffrence them

# convert the strings to regular integer number

# add value entered and store in sum

# substract value entered and store in difference
# multiply the number entered and store in product
# devide
# use modulus
'''

num1, num2 = input('Enter 2 numbers: ').split()

# convert the strings to regular integer number

num1 = int(num1)

num2 = int(num2)

# add value entered and store in sum

sum = num1 + num2

# substract value entered and store in difference
diff = num1 - num2
# multiply the number entered and store in product
product = num1 * num2

# devide printing quotient

devide = num1 * num2

# use modulus
modulo = num1 % num2

print("{} + {} = {}".format(num1, num1, sum))
print("{} - {} = {}".format(num1, num2, diff))
print("{} * {} = {}".format(num1, num2, product))
print("{} / {} = {}".format(num1, num2, devide))
print("{} % {} = {}".format(num1, num2, modulo))