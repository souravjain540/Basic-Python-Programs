def emi_calculator(p:float, r:float, t:float):
    """EMI Calculator for one months
    --------------------------------
    Parameters:
      p - principal 
      r - interest rate per month
      t - time period (in years)
    """
    r = r / (12 * 100) # one month interest
    t = t * 12 # one month period
    emi = (p * r * pow(1 + r, t)) / (pow(1 + r, t) - 1)
    return emi
 

principal = float(input("Enter principal amount (in ₹):"))
rate = float(input("Enter Interest Rate per month (%):"))
time = float(input("Enter Time period (in years):"))
emi = emi_calculator(principal, rate, time)
print("Your Monthly EMI is ₹", round(emi,2))
 
