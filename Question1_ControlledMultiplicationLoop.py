def find_factorial_exceeding_threshold(threshold):
    product = 1
    current_number = 1

    # Continue multiplying until the product exceeds the threshold
    while product <= threshold:
        # Increase current_number by 1 for the next multiplication
        current_number += 1
        # Multiply the current product by current_number
        product *= current_number

    # Return both the final number and the product that exceeded the threshold
    return current_number, product

def main():
    threshold = 100
    # Call the function and unpack the returned values
    current_number, product = find_factorial_exceeding_threshold(threshold)

    # Display results
    print(f"Final product: {product}")
    print(f"Integer that exceeded threshold: {current_number}")

main()