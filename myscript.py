"""Test for usage of magic command ~ % in ipython"""
def square(x):
    """Return the square of a number"""
    return x ** 2

for N in range(1,4):
    print(f"{N} is square of {square(N)}")