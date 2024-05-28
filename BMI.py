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

def main():
    # Get weight and height from the user
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))
    
    # Calculate BMI
    bmi = calculate_bmi(weight, height)
    
    # Output the result
    print(f"Your BMI is: {bmi:.2f}")

if __name__ == "__main__":
    main()
