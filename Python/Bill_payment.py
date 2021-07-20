# Split string method
import random

names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

length_of_list = (len(names))
random_name = random.randint(0, length_of_list - 1)
person_who_will_pay = names[random_name]

# person_who_will_pay = random.choice(names)
print(f"{person_who_will_pay} is going to buy the meal today!")
