# mortgage.py
#
# Exercise 1.7
#
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000
months_paid = 0
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    months_paid = months_paid + 1 # the location of this makes a difference!
    if principal < payment:
        total_paid = total_paid + principal
        principal = 0
    else:
        principal = principal * (1+rate/12) - payment
        total_paid = total_paid + payment
    if months_paid >= extra_payment_start_month and months_paid <= extra_payment_end_month:
        if principal < extra_payment:
            total_paid = total_paid + principal
            principal = 0
        else:
            principal = principal - extra_payment
            total_paid = total_paid + extra_payment
    print(months_paid,round(total_paid,2),round(principal,2))
print(f"Total paid {round(total_paid,1)}\nMonths {months_paid}")
