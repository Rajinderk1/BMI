def calculate_bmi(weight, height):
    """
    Calculate the Body Mass Index (BMI).

    Parameters:
    weight (float): Weight in kilograms
    height (float): Height in meters

    Returns:
    float: BMI value
    """
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    """
    Classify the BMI value.

    Parameters:
    bmi (float): BMI value

    Returns:
    str: Classification based on the BMI value
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    # Get weight and height from the user
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    
    # Classify BMI
    classification = classify_bmi(bmi)
    
    # Output the result
    print(f"Your BMI is: {bmi:.2f}")
    print(f"You are classified as: {classification}")

if __name__ == "__main__":
    main()
