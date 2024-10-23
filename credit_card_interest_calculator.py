import math

netBalance = float(input("Enter your net Balance: "))
paymentAmount = float(input("How much did you pay?: "))
d1 = int(input("How many days are in the billing cycle?:"))
d2 = int(input("How many days are left in the billing cycle?:"))

interest = float(input("what is your interst rate?(in percentage form):"))

avgDailyBalance = (netBalance * d1 - paymentAmount *d2)/d1

interest = avgDailyBalance * (interest / 100)

print(f"The interest incurred on this account for this billing cycle is: ${round(interest,2)}")
print(f"The ineterst incurred on this account for this billing cycle is: ${interest:.2f}")
                              
