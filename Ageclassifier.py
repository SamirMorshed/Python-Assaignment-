age = int(input("enter your age:"))


if age >= 0 and age <= 1:
    print("youre a infant :")
elif age >= 2 and age <=3:
    print("you're a toddler :")
elif age >= 4 and age <= 12:
    print("you're a child")
elif age >= 13 and age <= 19:
    print("you're a teenager")
elif age >= 20:
    print("you're a adult :")
else:
    print("wrong input")