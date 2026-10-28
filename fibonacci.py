"""
Fibonacci Sequence Generator
Author: Manik Kukkar
University: JECRC University, Jaipur
Description: Generates Fibonacci sequence and finds the nth Fibonacci number efficiently.
"""

def fibonacci_sequence(terms: int) -> list[int]:
    """Generate the first `terms` numbers of the Fibonacci sequence."""
    if not isinstance(terms, int):
        raise TypeError("Number of terms must be an integer.")
    if terms <= 0:
        return []
    if terms == 1:
        return [0]
    seq = [0, 1]
    while len(seq) < terms:
        seq.append(seq[-1] + seq[-2])
    return seq

def fibonacci_nth(n: int) -> int:
    """Find the nth Fibonacci number (0-indexed)."""
    if n < 0:
        raise ValueError("Index cannot be negative.")
    if n in (0, 1):
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def main():
    print("=== Fibonacci Generator (Manik Kukkar) ===")
    terms = 10
    print(f"First {terms} Fibonacci numbers: {fibonacci_sequence(terms)}")
    print(f"The 10th Fibonacci number is: {fibonacci_nth(10)}")

if __name__ == "__main__":
    main()
