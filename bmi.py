def calculate_bmi(height, weight):
    # Calculate BMI using the formula
    bmi = weight / (height * height)
    
    # Classify BMI into weight categories
    if bmi > 25.0:
        return 1  # Overweight
    elif bmi <= 25.0 and bmi >= 18.5:
        return 0  # Normal weight
    else:
        return -1  # Underweight

# Call the function and store the result
result = calculate_bmi(weight=45, height=1.9)

# Print the result
print("Weight classification:", result)