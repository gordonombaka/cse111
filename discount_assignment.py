"""
You work for a retail store that wants to increase sales on Tuesday and Wednesday, 
which are the store’s slowest sales days. On Tuesday and Wednesday, 
if a customer’s subtotal is $50 or greater, the store will discount the customer’s subtotal by 10%.
"""
# Import the datetime class from the datetime
# module so that it can be used in this prog

from datetime import datetime
current_date_and_time = datetime.now()
day_of_week = current_date_and_time.weekday()
day_of_week = 2


# User inputs

sub_total = float(input("Please enter the subtotal: "))

# Computation

if sub_total >= 50 and (day_of_week == 2 or day_of_week == 3):
    discount = 0.10 * sub_total
    total = sub_total - discount
    tax = total * 0.06
    grand_total = total + tax
    print(f"Sales tax amount is: ${tax:.2f}")
    print(f"Discount awarded is: ${discount:.2f}")
    print(f"Total amount is: ${grand_total:.2f}")
else:
    tax = sub_total * 0.06
    grand_total = tax + sub_total
    print(f"Sales tax amount is: ${tax:.2f}")
    print(f"Total amount is: ${grand_total:.2f}")


    
    

    

