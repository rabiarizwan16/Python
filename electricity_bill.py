fixed_rental_charges=250
first_100_unit_charges=3.25 #per unit
after_100_unit_charges=4.75  #per unit
tax=0.115

customer_num=input("Enter Customer Number:- ")
customer_name=input("Enter Customer Name:- ")
old_units=input("Enter the old reading units:- ")
current_units=input("Enter the current reading units:- ")

if old_units<current_units:
    total_consume = int(current_units) - int(old_units)
    new_consume = int(total_consume) - 100
    new_consume_bill=(new_consume) * (after_100_unit_charges)
    first_100_unit_bill=100*first_100_unit_charges
    total_usage=new_consume_bill + first_100_unit_bill
    total_tax=tax * total_usage
    total_bill=total_usage + total_tax + fixed_rental_charges

    print("               *******************************************************************************               ")
    print("                                           DELHI VIDHUT BOARD                                                            ")
    print("                                     Bill of supply for electricity                                                  ")
    print("            Circle: Delhi                      Circle code: 103                       Phone Number: 011-399999707")
    print("                  ---------------------------------------------------------------------------------                  ")
    print("                  Customer Number:                                             ", customer_num)
    print("                  Customer Name:                                               ", customer_name)
    print("                  Old Meter Reading:                                           ", old_units)
    print("                  Current Meter Reading:                                       ", current_units)
    print("                  Total Unit Consumed:                                         ", total_consume)
    print("                  Fixed Rental & Line Maintanance Charges:                     ", fixed_rental_charges)
    print("                  Total Usage:                                                 ", total_usage)
    print("                  Total Tax: (11.5%)                                           ", total_tax)
    print("                  --------------------------------------------------------------------------------------           ")
    print("                  Total Bill Amount Payable:                                   ",  total_bill)
else:
     print("==================================Invlid Bill==========================================================")
