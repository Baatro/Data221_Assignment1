# Function to sort values and filter those greater than x
def sort_and_search_values_greater_than_x(values, x):
    # Sort the input values in ascending order
    sorted_values = sorted(values)
    # Filter values that are greater than x
    greater_than_x = [value for value in sorted_values if value > x]
    # Return both the sorted list and the filtered list
    return sorted_values, greater_than_x

def main():
    # Helper code provided by assignment instructions
    from random import random
    # Generate 20 random values between 0 and 1
    values = [random() for i in range(20)]
    # Generate a random threshold value
    x = random()
    
    # Call the function to sort and filter values
    sorted_values = sort_and_search_values_greater_than_x(values, x)
    # Print the values that exceeded the threshold
    print(f"Values greater than {x}: {sorted_values}")

# Run the main function
main()




