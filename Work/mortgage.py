principal = 500000
rate = 0.05
payment = 2684.11
total_paid = 0
months = 0

while principal > 0:
    if months < 12:
        payment = 3684.11
        principal = principal * (1 + rate/12) - payment
        total_paid += payment
        months += 1
    elif months >= 12:
        payment = 2684.11
        principal = principal * (1 + rate/12) - payment
        total_paid += payment
        months += 1

print(f"Total paid: {total_paid:.2f}")
print(f"Months: {months}")