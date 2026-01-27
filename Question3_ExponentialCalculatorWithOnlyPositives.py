def exponential_calculator_with_positives(list_of_pairs):
    calculated_values_of_exponents = [] # empty list to store calculated exponent values
    for base, exponent in list_of_pairs:
        if exponent < 0:
            raise ValueError("Exponent must be non-negative.") # Only positive exponents are allowed
        else:
            calculated_values_of_exponents.append(base ** exponent) # Once exponent is verified as positive, calculate the power :)
    return calculated_values_of_exponents
def main(): 
    pairs = [(2, 3), (4, 0), (5, 2)]
    print(exponential_calculator_with_positives(pairs))

main()