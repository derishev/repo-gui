src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
resalt = [number for counter, number in enumerate(src) if src[counter - 1] < number and counter != 0]
print(resalt)
