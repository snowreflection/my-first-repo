from typing import Iterable, List


def sort_numbers(numbers: Iterable[int]) -> List[int]:
    """Return a list of integers sorted in ascending order."""
    return sorted(numbers)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Sort numbers in ascending order.")
    parser.add_argument("numbers", nargs="+", type=int, help="Numbers to sort.")
    args = parser.parse_args()
    sorted_nums = sort_numbers(args.numbers)
    print(" ".join(str(n) for n in sorted_nums))

