
def estimate(a, b):
    sum = 0
    for index, val in enumerate(a):
        sum += ((float(val) - float(b[index])) ** 2)
    sum = sum / len(a)
    return sum ** (0.5)