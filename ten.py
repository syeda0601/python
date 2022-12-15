def test(combined):
    ls = []
    s2 = ""
    for s in combined.replace(' ', ''):
        s2 += s
        if s2.count("(") == s2.count(")"):
            ls.append(s2)
            s2 = ""
    return ls 
combined = '( ()) ((()()())) (()) ()'
print("Parentheses string:")
print(combined)
print("Separate parentheses groups of the said string:")
print(test(combined))