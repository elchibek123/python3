print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
tip = int(input("Waht percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = (bill * tip / 100) + bill

each = bill_with_tip / people

final_amount = round(each, 2)
final_amount = "{:.2f}".format(each)

print(f"Each person should pay: {final_amount}")