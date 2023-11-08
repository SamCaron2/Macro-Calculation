# Created by Sam Caron 11/7/2023
# This program calculates the recommended macronutrients and daily calories for gaining, maintaining, or losing weight.

def Macro_Calculator(weight, height, gender, age, amountOfActivity, goal):

    # Define the macronutrient ratios based on the user's goal
    if goal == 'lose':
        proteinRatio = 0.25  # Adjust protein ratio for weight loss
        carbRatio = 0.45  # Adjust carb ratio for weight loss
        fatRatio = 0.3  # Adjust fat ratio for weight loss
    elif goal == 'gain':
        proteinRatio = 0.3  # Adjust protein ratio for weight gain
        carbRatio = 0.55  # Adjust carb ratio for weight gain
        fatRatio = 0.15  # Adjust fat ratio for weight gain
    elif goal == 'maintain':
        # Use the default ratios
        proteinRatio = 0.3
        carbRatio = 0.5
        fatRatio = 0.2
    else:
        return "Invalid goal."

    # Calculate BMR based on gender
    if gender == 'male':
        bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == 'female':
        bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        return "Invalid gender type"

    # Calculate daily calorie needs based on activity level
    if amountOfActivity == 'none':
        activity_multiplier = 1.2
    elif amountOfActivity == 'light':
        activity_multiplier = 1.375
    elif amountOfActivity == 'moderate':
        activity_multiplier = 1.55
    elif amountOfActivity == 'high':
        activity_multiplier = 1.725
    elif amountOfActivity == 'extreme':
        activity_multiplier = 1.9
    else:
        return "Invalid activity level"

    # Calculate daily calories based on BMR and activity level
    calories = bmr * activity_multiplier

    # Calculate macronutrients based on the adjusted ratios and convert to grams
    carbsInGrams = (calories * carbRatio) / 4  # 1g of carbs = 4 calories
    proteinInGrams = (calories * proteinRatio) / 4  # 1g of protein = 4 calories
    fatInGrams = (calories * fatRatio) / 9  # 1g of fat = 9 calories

    return {
        'calories': calories,
        'carbsInGrams': carbsInGrams,
        'proteinInGrams': proteinInGrams,
        'fatInGrams': fatInGrams
    }

# Begin program screen
print("Welcome to the Macro Calculator!")
print("Please choose your preferred unit of measurement:")
print("1. US Units")
print("2. Metric Units")

unit= input("Enter 1 or 2 to select your preferred unit system: ")
# Since the Harris-Benedict formula uses metric we have to convert the US units to metric first
if unit == '1':
    weight = float(input("Enter your weight in pounds: "))
    height = float(input("Enter your height in inches: "))
    weight = weight * 0.45359237  # Convert pounds to kilograms
    height = height * 2.54  # Convert inches to centimeters
elif unit == '2':
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in centimeters: "))
else:
    print("Invalid choice. Please enter 1 or 2 to select your preferred unit system.")



age = int(input("Enter your age in years: "))
gender = input("Enter your gender (male or female): ").lower()
while gender not in ('male', 'female'):
    print("Invalid gender. Please enter 'male' or 'female.")
    gender = input("Enter your gender (male or female): ").lower()


amountOfActivity = input("Enter your weekly activity level (none, light, moderate, high, extreme): ").lower()
while amountOfActivity not in ('none', 'light', 'moderate', 'high', 'extreme'):
    print("Invalid activity level. Please enter 'none', 'light', 'moderate', 'high', or 'extreme'.")
    amountOfActivity = input("Enter your weekly activity level (none, light, moderate, high, extreme): ").lower()


goal = input("Enter your goal (maintain, lose, gain): ").lower()
while goal not in ('maintain', 'lose', 'gain',):
    print("Invalid goal. Please enter 'maintain', 'lose', 'gain'.")
    goal = input("Enter your goal (maintain, lose, gain): ").lower()

macros = Macro_Calculator(weight, height, gender, age, amountOfActivity, goal)

calories = macros['calories']
carbs_in_grams = macros['carbsInGrams']
protein_in_grams = macros['proteinInGrams']
fat_in_grams = macros['fatInGrams']

print("\nBased on your choices, here is your new recommended daily calorie and macronutrient intake:")
print(f"Daily Calories: {calories:.2f} calories")
print(f"Carbohydrates: {carbs_in_grams:.2f} grams")
print(f"Protein: {protein_in_grams:.2f} grams")
print(f"Fat: {fat_in_grams:.2f} grams")

