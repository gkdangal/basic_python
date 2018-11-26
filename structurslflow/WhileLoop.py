import random

# calculating randome number
rand_num = random.randrange(1, 50)

i = 1

while(i != rand_num):
    i += 1

print("The random value is : ", rand_num)

# Break and Continue

i = 1

while i <= 20:
    if (i % 2) == 0:
        i += 1
        continue
    if i == 15:
        break
    print("odd: ", i)
    i += 1

