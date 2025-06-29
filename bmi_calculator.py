print("📏 BMI Calculator")

height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))

bmi = weight / (height ** 2)
print(f"🧮 Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("⚠️ You're underweight.")
elif 18.5 <= bmi < 25:
    print("✅ You're in the healthy range.")
elif 25 <= bmi < 30:
    print("⚠️ You're overweight.")
else:
    print("🚨 You're in the obese range.")
