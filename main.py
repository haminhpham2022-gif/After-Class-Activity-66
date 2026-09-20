def bitDifference(a, b):
    counter = 0

    while a > 0 or b > 0:
        lastsetbit1 = a & 1
        lastsetbit2 = b & 1

        if lastsetbit1 != lastsetbit2:
            counter += 1

        a = a >> 1
        b = b >> 1

    return counter

print("== Check the bit difference between two numbers ==")
a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
print("")
print(f"The difference in bits is {bitDifference(a, b)}")
print(f"{a} = {bin(a)[2:]}; {b} = {bin(b)[2:]}")