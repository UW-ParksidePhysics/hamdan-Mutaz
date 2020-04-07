  
n = int(input("What value is n? "))
Sum1 = 0
for n in range(0, n+1):
    Sum1 = Sum1 + n
print("Sum of integers =", Sum1)

Sum2 = n * (n + 1) / 2
print("n(n+1)/2 =", Sum2)
