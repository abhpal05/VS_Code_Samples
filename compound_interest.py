# Formula to calculate compound interest annually is given by:
# A = P(1 + R/100) t
# Compound Interest = A – P
# Where,
# A is amount
# P is principle amount
# R is the rate and
# T is the time span

def getCompoundReturn(p, r, t):
    a = p*pow((1+(r/100)), t)
    return a


principal_amount = int(input('Enter Principal Amount: '))
interest_rate = int(input('Enter interest rate: '))
time_period = int(input('Enyer Tenure: '))

total_return = getCompoundReturn(principal_amount, interest_rate, time_period)
total_compoundInterest = total_return - principal_amount

print('Your Principal Amount: ' + str(principal_amount))
print('Your Interest Rate: ' + str(interest_rate))
print('Your time period: ' + str(time_period))
print('Your total return: ' + str(total_return))
print('Your total Compound Interest: ' + str(total_compoundInterest))
