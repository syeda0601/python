def test(string):
    import re
    merged = re.split(r"([ ,]+)", string)
    return [merged[::2], merged[1::2]]
s = "Python Internship, program."
print("Original string:",s)
print("Split the said string into 2 lists: words and separators:")
print(test(s))