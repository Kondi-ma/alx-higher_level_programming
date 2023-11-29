#!/usr/bin/python3
for a in range(9):
    for b in range(a + 1, 10):
         if a * 10 + b < 89:
            print("{}{}".format(a, b), end=", ")
print("{}".format(89))


