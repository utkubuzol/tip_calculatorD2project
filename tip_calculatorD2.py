#If the bill was $150.00, split between 5 people, with 12% tip. 
print("Welcome to the tip calculator!\n")
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
bill = input("What was the total bill? ")
bill_is_float = float(bill)
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
tip = input("How much tip would you like to give? 10, 12, or 15? ")
tip_is_int = int(tip)
#Write your code below this line 👇
split = input("How many people to split the bill? ")
split_is_int = int(split)
result = ((((tip_is_int / 100)*(bill_is_float)) + bill_is_float) / split_is_int )
print(f"Each person should pay: {result} ")