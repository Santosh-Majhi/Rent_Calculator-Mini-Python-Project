# rent = int(input("Enter your hostel/flat rent = "))
# food = int(input("Enter the amount of food ordered = "))
# electricity_spend = int(input("Enter the total of electricity spend in unit = "))
# charge_per_unit = int(input("Enter the charge per unit = "))
# persons = int(input("Enter the number of persons living in room/flat = "))

# total_bill = electricity_spend * charge_per_unit

# output = (food + rent + total_bill) // persons

# print("Each person will pay = ", output)


try:
    rent = int(input("Enter your hostel/flat rent: "))
    food = int(input("Enter the amount spent on food: "))
    electricity_spend = int(input("Enter the total electricity consumption (in units): "))
    charge_per_unit = int(input("Enter the charge per unit of electricity: "))
    persons = int(input("Enter the number of persons living in the room/flat: "))

    if persons <= 0:
        raise ValueError("Number of persons must be greater than zero.")

    electricity_bill = electricity_spend * charge_per_unit

    
    total_cost = rent + food + electricity_bill
    per_person_cost = total_cost // persons

    print(f"Each person will pay: {per_person_cost}")

except ValueError as ve:
    print(f"Input error: {ve}. Please enter valid numbers.")
except ZeroDivisionError:
    print("Error: Division by zero occurred. Ensure the number of persons is greater than zero.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")