# Calculate cc balance after 1 year of minimum payments (2%)

balance = float(input('Enter the outstanding balance on your credit card: '))
annual_interest = float(input('Enter the annual credit card interest rate as a decimal: '))
minimum_rate = float(input('Enter the minimum monthly payment rate as a decimal: '))

month = 1
total = 0

while month <= 12:

    minimum_payment = round(balance * minimum_rate, 2)
    interest_paid = round(annual_interest / 12 * balance, 2)
    principal_paid = round(minimum_payment - interest_paid, 2)
    balance = round(balance - principal_paid, 2)

    print('Month: ' + str(month))
    print('Minimum monthly payment: $' + str(minimum_payment))
    print('Principle paid: $' + str(principal_paid))
    print('Remaining balance: $' + str(balance))

    month += 1

    total = round(total + minimum_payment, 2)

print('RESULT')
print('Total amount paid: $' + str(total))
print('Remaining balance: $' + str(balance))
