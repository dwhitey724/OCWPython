# Calculates minimum fixed monthly payment needed to pay off cc balance within 12 months

balance = float(input('Enter the outstanding balance on your credit card: '))
annual_interest = float(input('Enter the annual credit card interest rate as a decimal: '))

month = 1
monthly_interest = annual_interest / 12
monthly_payment = 10

while month <= 12:
    original_balance = balance
    balance = round(balance * (1 + monthly_interest) - monthly_payment, 2)
    month += 1

    if balance >= 0:
        monthly_payment += 10
        balance = original_balance
        month = 1
    else:
        break

print('RESULT')
print('Monthly payment to pay off debt in 1 year: ' + str(monthly_payment))
print('Number of months needed: ' + str(month))
print('Balance: ' + str(balance))
