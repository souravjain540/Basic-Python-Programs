def get_amortization_amount(principal, interest_rate, period):
    x = (1 + interest_rate) ** period
    amort_amount = principal * (interest_rate * x) / (x - 1)    
    return amort_amount 


def get_amortization_table(principal, interest_rate, period):
    amortization_amount = get_amortization_amount(principal, interest_rate, period)
    number = 1
    balance = principal
    while number <= period:
        interest = balance * interest_rate
        principal = amortization_amount - interest
        balance = balance - principal
        yield number, round(amortization_amount, 2), round(interest,2), round(principal,2), round(balance,2) if balance > 0 else 0
        number += 1


principal = 20000
interest_rate = 8/100/12
nperiods = 5 * 12


amortization_list = list(get_amortization_table(principal, interest_rate, nperiods))
print ('%-8s' % 'nper', '%-12s' % 'interest', '%-12s' % 'principal',  'balance')
print ('--------------------------------------------')
for x in amortization_list:
  print ('%-8i' % x[0], '%-12.2f' % x[2], '%-12.2f' % x[3], x[4])
