# This is the for loop on python

# loop with in list

for i in [2, 4, 5, 6, 7, 8]:
    print(i)

print('for loop in range:')
for i in range(10):
    print(i)

print('for loop in range:')
for i in range(2, 10):
    print('i = ',i)

# Another method for loop

print('Printing even and odd number: ')
n = 0
for j in [3, 5, 7, 8, 9, 3, 4, 7]:
    if j % 2 == 0:
        n=n+1
        # print("even i = ", j)
    else:
        print()
        # print("even i = ", j)
print('number of even is: ', n)

