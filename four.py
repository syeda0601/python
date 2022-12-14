def test(n):    
    return [n + 2 * i for i in range(n)]   
n = 2
print("Number of piles:",n)
print("Number of stones in each pile:")
print(test(n)) 