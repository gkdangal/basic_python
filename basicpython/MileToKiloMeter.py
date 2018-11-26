# In this program i am going to convert miles to kilometer and Fahrenheit to celsius

# I am taking 2 input followed by space seperation one is miles and another is temperature on fahrenheit

miles, fahren = input(" Enter two number followed by space: ").split()

miles = float(miles)
fahren = float(fahren)

kilometers = miles * 1.60934

celsius = (fahren-32)*100/180


print("{} miles = {} kilometers".format(miles,kilometers))


print("{} .f= {} .c".format(fahren, celsius))