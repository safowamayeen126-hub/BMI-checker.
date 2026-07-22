# Project: BMI Checker
# Name: Safowa Mayeen (Captain), Araf (Member), Sourjo (Member), Kabbo (Member)

print("      WELCOME TO BMI CHECKER      ")

print("\nEnter Your Information")
print("-" * 27)

# Weight Input Validation
while True:
    try:
        weight = float(input("Enter your weight (kg): "))

        if weight > 0:
            break
        else:
            print("Weight must be greater than 0!")

    except:
        print("Please enter numbers only!")

# Height Input Validation
while True:
    try:
        height_cm = float(input("Enter your height (cm): "))

        if height_cm > 0:
            break
        else:
            print("Height must be greater than 0!")

    except:
        print("Please enter numbers only!")

# Convert cm to meter
height = height_cm / 100

# BMI Calculation
bmi = weight / (height ** 2)

print(f"\nYour BMI is: {bmi:.2f}")

# BMI Category
if bmi < 18.5:
    print("Category: Underweight")
    print("-" * 10)
    print("Advice: Eat nutritious foods and consult a doctor if needed.")
    print("-" * 8)

elif bmi < 25:
    print("Category: Normal Weight")
    print("-" * 10)
    print("Advice: Great! Maintain your healthy lifestyle.")
    print("-" * 8)

elif bmi < 30:
    print("Category: Overweight")
    print("-" * 10)
    print("Advice: Exercise regularly and reduce junk food.")
    print("-" * 8)

else:
    print("Category: Obese")
    print("-" * 10)
    print("Advice: Consult a doctor and start a healthy diet plan.")
    print("-" * 8)

print("\nThank you for using BMI Checker!")
print("Stay Healthy & Have a Nice Day!")