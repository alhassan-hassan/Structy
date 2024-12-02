def is_palindrome(x: int) -> bool:
    # Negative numbers are not palindromes
    # Numbers that end with 0 and are not 0 themselves are also not palindromic
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reversed_half = 0
    while x > reversed_half:
        # Take the last digit of x and add it to the reversed_half
        reversed_half = reversed_half * 10 + x % 10
        # Remove the last digit from x
        x //= 10
    
    # Check if the number is palindromic
    print(x, reversed_half)
    return x == reversed_half or x == reversed_half // 10

print(is_palindrome(1001))