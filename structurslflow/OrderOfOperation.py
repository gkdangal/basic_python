
# This is not important program but want to test Order of operation

print("3 + 4 * 5 = {}".format(3 + 4 * 5))

print("(3 + 4) * 5 = {}".format((3 + 4) * 5))

# 2 * { (3 + 4) - 5 } -2
print("2 * [5 + (3 + 4) - 5 ] -2 = {}".format(2 * (5 + (3 + 4) - 5) - 2))
