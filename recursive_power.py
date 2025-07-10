def Power(a,b):
    if b == 0:
        return 1
    if a == 1:
        return 1

    return a * Power(a,b-1)
