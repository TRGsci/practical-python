principal = 500000
rate = 0.05
payment = 0
total_paid = 0
months =0

extra_payment_start_month = 60
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    if extra_payment_start_month <= months < extra_payment_end_month:
        print(f'Month: {months},Amount paid: {payment + extra_payment:.2f}, Remaining principal: {principal:.2f}')
        payment = 2684.11 + extra_payment
        principal = principal * (1 + rate/12) 
        payment = min(payment, principal)
        principal -= payment
        total_paid += payment
        months += 1
    elif months < extra_payment_start_month or months >= extra_payment_end_month:
        print(f'Month: {months},Amount paid: {payment:.2f}, Remaining principal: {principal:.2f}')
        payment = 2684.11
        principal = principal * (1 + rate/12) 
        payment = min(payment, principal)
        principal -= payment
        total_paid += payment
        months += 1


print(f"Total paid: {total_paid:.2f}")
print(f"Months: {months}")