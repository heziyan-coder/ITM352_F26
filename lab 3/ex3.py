def squareroot(n):
    """Return the square root of a number n."""
    if n < 0:
        raise ValueError("Cannot compute the square root of a negative number.")
    return n ** 0.5

print(squareroot(16))