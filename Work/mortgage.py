# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000.0


while principal > 0:
    month = month + 1
    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        total_payment = round(payment + extra_payment,2)
    else:
        total_payment = round(payment,2)
        
    if total_payment > principal:
        total_payment = round(principal,2)
        
    principal = round(principal * (1 + rate/12) - total_payment,2)
    total_paid = round(total_paid + total_payment,2)
    print(month,total_paid,principal)
    
print ('Total paid:', total_paid)
print ('Total months:', month)
