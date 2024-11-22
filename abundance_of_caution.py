def percent_to_string(value):
    """

    Args:
        value (float): A float value between 0.0 and 1.0.

    Returns:
        str: The percentage as a string with no decimal places, e.g., '25%'.
    """
    if type(value) != float:
        raise TypeError("Must be a float")

    if 0.0 <= value <= 1.0:
        return round(value * 100) + "%"
    else:
        raise ValueError("Value must be between 0.0 and 1.0.")
    
def main():
    user_input = input("give number")
    print(percent_to_string(user_input))
    

if __name__ == "__main__":
    main()