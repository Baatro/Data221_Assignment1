def distribution_analysis(list_of_numbers):
    unique_numbers_less = {}

    for number in list_of_numbers:
        if number not in unique_numbers_less:
            count_of_numbers_less_than_number = 0
            for compare_number in list_of_numbers:
                if compare_number < number:
                    count_of_numbers_less_than_number += 1
            unique_numbers_less[number] = count_of_numbers_less_than_number

    return unique_numbers_less


def main():
    numbers = [3, 1, 2, 3, 4, 2]
    print(distribution_analysis(numbers))

main()
