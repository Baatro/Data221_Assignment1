import math

def circle_area_compare(radius1, radius2):
    # sanity check radii
    if radius1 < 0 or radius2 < 0:
        raise ValueError("Radius cannot be negative")

    # calculate area of each circle
    area_circle1 = math.pi * radius1**2
    area_circle2 = math.pi * radius2**2

    # figure out which circle is larger
    largest_circle = max(area_circle1, area_circle2)
    smaller_circle = min(area_circle1, area_circle2)

    # calculate coverage
    covered_area = (smaller_circle / largest_circle) * 100
    return covered_area


def main():
    radius_of_circle1 = 3
    radius_of_circle2 = 5

    print(f"The smaller circle covers {circle_area_compare(radius_of_circle1, radius_of_circle2)}% of the larger one.")


main()