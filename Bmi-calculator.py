
height = float(input("enter your height in M :"))

weight = float(input("enter your weight in kg :"))

bmi = weight / height ** 2

if bmi < 18.5 :
    print("you are underweight :")
elif bmi <= 24.9:
    print("you are healthy")
elif bmi <= 29.9:
    print ("you are overweight")
else:
    print("you are obese")
