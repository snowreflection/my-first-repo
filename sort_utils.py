def sort_numbers(numbers):
    """Return a list of numbers sorted in ascending order."""
    return sorted(numbers)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Sort numbers in ascending order.")
    parser.add_argument("numbers", nargs="+", type=float, help="Numbers to sort.")
    args = parser.parse_args()
    sorted_nums = sort_numbers(args.numbers)
    print(sorted_nums)

