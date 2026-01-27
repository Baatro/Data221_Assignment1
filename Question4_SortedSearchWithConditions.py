def sort_and_search_values_greater_than_x(values, x):
    sorted_values = sorted(values)
    greater_than_x = [value for value in sorted_values if value > x]
    return sorted_values, greater_than_x

def main():
    from random import random
    values = [random() for i in range(20)]
    x = random()
    print(f"Values greater than {x}: {values}")

main()




