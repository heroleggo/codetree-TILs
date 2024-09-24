def check(original, substr):
    for i in range(0, len(original) - len(substr) + 1):
        if original[i:i+len(substr)] == substr:
            return i
    return -1

orig = input()
sub = input()

print(check(orig, sub))