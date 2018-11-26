# if condition on python

num1, operator, num2 = input('Please enter 1st number Operator and second number seperated by space: ').split()

num1 = float(num1)
num2 = float(num2)

if operator == "+":
    print('we are going to add')
    print('{} + {} = {}'.format(num1, num2, num1 + num2))
elif operator == "-":
    print('we are going to substract')
    print('{} - {} = {}'.format(num1, num2, num1 - num2))
elif operator == "*":
    print('we are going to multiply')
    print('{} * {} = {}'.format(num1, num2, num1 * num2))
elif operator == "/":
    print('we are going to devide')
    print('{} / {} = {}'.format(num1, num2, num1 / num2))
else:
    print("'Please enter 1st number Operator and second number Next time")
