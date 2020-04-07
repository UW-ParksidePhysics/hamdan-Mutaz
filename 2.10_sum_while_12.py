# s = 0; k = 1; M = 100
# while k < M:
#    s += 1 / k
# print s

s = 0
k = 1
M = 100
while k <= M:
    s += 1 / k
    k += 1
print(s)

# 1) k wasn't being added one every cycle, thus k would never reach M
# 2) k must be less than OR EQUAL to M, not just less than, as this excludes the term 100
# 3) Placed parentheses around what was intended to be printed
