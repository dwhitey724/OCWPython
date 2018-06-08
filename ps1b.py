# Calculates minimum fixed monthly payment needed to pay off cc balance within 12 months

balance = float(input('Enter the outstanding balance on your credit card: '))
annual_interest = float(input('Enter the annual credit card interest rate as a decimal: '))

monthly_interest = annual_interest / 12
monthly_payment = 10

original_balance = balance  # Initialize value to reset balance after iterating

while balance > 0:
    for month in range(1, 13):
        balance = round(balance * (1 + monthly_interest) - monthly_payment, 2)  # Calculate if balance goes negative
        if balance < 0:  # If yes, stop calculating
            break
    if balance > 0:  # If the monthly payment never gets balance to go negative, reset and try with higher number
        balance = original_balance
        monthly_payment += 10
    else:
        break

print('RESULT')
print('Monthly payment to pay off debt in 1 year: ' + str(monthly_payment))
print('Number of months needed: ' + str(month))
print('Balance: ' + str(balance))
