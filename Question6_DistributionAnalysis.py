def distribution_analysis(list_of_numbers):
    #create empty dictionary to store unique numbers and their counts of numbers less than them
    unique_numbers_less = {}

# Iterate through each number in the list
    for number in list_of_numbers: 
        # If the number is not already processed
        if number not in unique_numbers_less:
            count_of_numbers_less_than_number = 0
            for compare_number in list_of_numbers:
                if compare_number < number:
                    # Increment count if compare_number is less than the current number
                    count_of_numbers_less_than_number += 1
            unique_numbers_less[number] = count_of_numbers_less_than_number
# Return the dictionary with unique numbers and their counts
    return unique_numbers_less

# testing using the expected output
def main():
    numbers = [3, 1, 2, 3, 4, 2]
    print(distribution_analysis(numbers))

main()
