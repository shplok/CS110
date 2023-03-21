import stdio
import sys


# Entry point [DO NOT EDIT].
def main():
    s = sys.argv[1]
    stdio.writeln(_isPalindrome(s))


# Returns True if s is a palindrome, and False otherwise.
def _isPalindrome(s):
    # Base case: if s is the empty string, return True.
    if s == "":
        return "True"

    # Recursive step: return True if the first and last characters of s are the same and
    # _isPalindrome(characters between first and last in s) is True; and False otherwise.
    return "True" if s[0] == s[-1] and _isPalindrome(s[1:-1]) == "True" else False


if __name__ == '__main__':
    main()
