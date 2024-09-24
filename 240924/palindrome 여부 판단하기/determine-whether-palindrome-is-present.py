import math

def isPalindrome(string):
    half = int(len(string) / 2)
    for i in range(0, half):
        if string[i] != string[len(string) - 1 - i]:
            return "No"
    return "Yes"

data = input()

print(isPalindrome(data))