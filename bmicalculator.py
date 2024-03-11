height=float(input("enter your height in centimeters :"))
weight=float(input("enter your weight in kilograms :"))
bmi=weight / (height/100)**2 # this is the formula tom calculate bmi
print("your bmi is ",bmi)
if bmi<=18.5:
    print ("you are underweight")
elif bmi<=24.9:
    print("you are normal weight ")
elif bmi<=29.9:
    print("you are overweight")
else:
    print("you are obese")