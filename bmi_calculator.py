height = float(input("Height in m: "))
weight = float(input("Weight in kg: "))
bmi = weight / (height * height)
bmistr = str(bmi)
print("The BMI is " + bmistr)