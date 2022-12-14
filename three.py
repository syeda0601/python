def test(n):
    return n % 34 == 4 and n > 4 ** 4

n = 922
print("Original Integer:")
print(n)
print("Check whether the said integer greater than 4^4 and which is 7 mod 134 :")
print(test(n))