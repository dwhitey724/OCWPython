# Calculates minimum fixed monthly payment needed to pay off cc balance within 12 months
# but better than last time (with bisection search and more refined values)

balance = float(input('Enter the outstanding balance on your credit card: '))
annual_interest = float(input('Enter the annual credit card interest rate as a decimal: '))

monthly_interest = float(annual_interest / 12)

lower_bound = float(balance / 12)
upper_bound = float((balance * (1 + monthly_interest) * 12) / 12)
convergence = 0.01

original_balance = balance  # Initialize value to reset balance after iterating

while abs(balance) > convergence:
    midpoint = (lower_bound + upper_bound) / 2  # Calculate new midpoint, use as minimum payment
    balance = original_balance  # Reset balance
    for month in range(1, 13):
        balance = balance * (1 + monthly_interest) - midpoint  # Calculate remaining balance
    if balance > convergence:  # If remaining balance is too high, take upper half of values
        lower_bound = midpoint
    elif balance < -convergence:  # If remaining balance is too low, take lower half of values
        upper_bound = midpoint
    else:
        break

print('RESULT')
print('Monthly payment to pay off debt in 1 year: ' + str(round(midpoint, 2)))
print('Number of months needed: ' + str(month))
print('Balance: ' + str(round(balance, 2)))
