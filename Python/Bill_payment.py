import random
names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")

length_of_list = (len(names))
random_name = random.randint(0, length_of_list - 1)
person_who_will_pay = names[random_name]

print(f"{person_who_will_pay} is going to buy the meal today!")
