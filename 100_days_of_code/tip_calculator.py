#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print('The Tip Calculator')
total_bill = input('What was the total bill?')
tipPercentage = input('What percentage tip would you like to give? 10, 12, or 15?')
num_People = input('How many people to split the bill?')
result = (float(total_bill) / int(num_People)) * (1 + int(tipPercentage)/100)
roundedResult = round(result, 2)
print(roundedResult)
