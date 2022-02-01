#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇

intro_message = "Welcome to the tip calculator!"
print(intro_message)
total_bill = float(input("What was the total bill? "))
tip_percent_choice = round(float(input("How much tip would you like to give? 10, 12, or 15? ")) / 100, 2)
num_people = int(input("How many people to split the bill? "))

total_tip = round(total_bill * tip_percent_choice, 2)
total_with_tip = round(total_bill + total_tip, 2)
amount_per_person = round(total_with_tip / num_people, 2)
# got everything on my own except the formatting of the decimal places, 
# i thought i had a math error somewhere had to reference the video and 
# google to sort out the issue
amount_per_person = "{:.2f}".format(amount_per_person)

tip_message = f"Each person should pay: ${amount_per_person}"
print(tip_message)