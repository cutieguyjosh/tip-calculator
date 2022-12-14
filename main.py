#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? $")
tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
split = input("How many people are splitting the bill? ")

new_total_bill = float(total_bill)
new_tip = int(tip)
new_split = int(split)

payment_split = (new_total_bill / new_split) * ((100 + new_tip) * .01)
new_payment_split = round(payment_split, 2)
new_payment_split = "{:.2f}".format(new_payment_split)

print(f"Each person should pay: ${new_payment_split}")


