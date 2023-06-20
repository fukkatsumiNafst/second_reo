def polynd(d):
    if d == d[::-1]:
        return True
    else:
        return False

a = input()
print(polynd(a))