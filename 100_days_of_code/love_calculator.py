# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆


#Write your code below this line 👇
name1 = name1.lower()
name2 = name2.lower()

name3 = name1 + name2

# Counting the occurrence of each letter in word TRUE in both the names
total_true = name3.count('t') + name3.count('r') + name3.count('u') + name3.count('e')

# # Counting the occurrence of each letter in word LOVE in both the names
total_love = name3.count('l') + name3.count('o') + name3.count('v') + name3.count('e')

# Adding 
total_combined = str(total_true) + str(total_love)

if int(total_combined) < 10 or int(total_combined) > 90:
    print(f'Your score is {total_combined}, you go together like coke and mentos.')
elif int(total_combined) >= 40 and int(total_combined) <= 50:
    print(f'Your score is {total_combined}, you are alright together.')
else:
    print(f'Your score is {total_combined}.')