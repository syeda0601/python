def test(str1):
    return str1[len(str1)-2] in str1[len(str1)-1] and str1[len(str1)-2] != str1[len(str1)-1]

str11 = ["a","abb","sfs", "oo", "de", "sfde"]
print("Original list:")
print(str11)
print("Check the nth-1 string is a proper substring of nth string of the said list of strings:")
print(test(str11))