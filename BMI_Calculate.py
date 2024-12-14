print("======================== BMI TABLE ==========================")
print("               Classification        BMI range- kg/m2")
print("             -------------------    -------------------")
print("               Severe Thinness	        < 16")
print("               Moderate Thinness	    16 - 17")
print("               Mild Thinness            17 - 18.5")
print("               Normal	                18.5 - 25")
print("               Overweight	            25 - 30")
print("               Obese Class I	        30 - 35")
print("               Obese Class II     	    35 - 40")
print("               Obese Class III	        > 40")



height=float(input("Enter height (in meter): "))
weight=float(input("Enter weight (in kg): "))
BMI=float(weight/(height*height))
BMI=round(BMI,2)
print(f"Your BMI range is: {BMI}")
if BMI < 16:
    category = "Severe Thinness"
elif 16 <= BMI < 17:
    category = "Moderate Thinness"
elif 17 <= BMI < 18.5:
    category = "Mild Thinness"
elif 18.5 <= BMI < 25:
    category = "Normal"
elif 25 <= BMI < 30:
    category = "Overweight"
elif 30 <= BMI < 35:
    category = "Obese Class I"
elif 35 <= BMI < 40:
    category = "Obese Class II"
else:
    category = "Obese Class III"


print(f"Your BMI category is: {category}")