# John Rey Bulfa
# ITELEC2
# Laboratory #17 – Guided Coding Exercise:
# Variables, Literals, and Case-Sensitivity in Python (with Naming Conventions)

def main():
    def square(num):
        """Returns the square of the given number."""
        return num * num  # Or num ** 2
    def sum_of_squares(numbers):
        """Returns the sum of the squares of the numbers in the list."""
        total = 0
        for n in numbers:
            total += square(n)  # Call the square function and add to total
        return total
    numbers_list = [2, 3, 4]
    result = sum_of_squares(numbers_list)
    print(f"The sum of squares is: {result}")

if __name__ == "__main__":
    main()