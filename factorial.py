"""
Factorial Calculation Program
Author: Manik Kukkar
University: JECRC University, Jaipur
Description: Iterative and recursive implementations of factorial calculation with edge-case handling.
"""

def factorial_iterative(n: int) -> int:
    """Calculate factorial of n iteratively."""
    if not isinstance(n, int):
        raise TypeError("Factorial is only defined for integers.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n: int) -> int:
    """Calculate factorial of n recursively."""
    if not isinstance(n, int):
        raise TypeError("Factorial is only defined for integers.")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n in (0, 1):
        return 1
    return n * factorial_recursive(n - 1)

def main():
    print("=== Factorial Calculation (Manik Kukkar) ===")
    test_values = [0, 1, 5, 7, 10]
    for val in test_values:
        print(f"factorial({val}) -> Iterative: {factorial_iterative(val)}, Recursive: {factorial_recursive(val)}")

if __name__ == "__main__":
    main()
