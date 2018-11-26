# here i am going to calculate compound interest

# for this we are going to use pow function to calculate compound interest
# in floating number after 16 decimal number i.e. bogus (value less)


principle_amount = float(input('Enter the Principle Amount: '))

comInterestRate = float(input('Enter the Interest rate: '))

timePeriod = float(input('Enter the time in year Amount: '))

future_value = principle_amount * pow((1 + comInterestRate / 100), timePeriod)

print('Tottal amount: {:.4f} '.format(future_value))



