prime_numbers = []
N = int(input("Find all the prime numbers between 0 and ? "))

for i in range(2, N + 1):
    prime_numbers.append(i)

w = 2
while w < len(prime_numbers):
    element = prime_numbers[w]
    if element % 2:
        0
    else:
        prime_numbers.pop(w)
    w += 1
w = 2
while w < len(prime_numbers):
    element = prime_numbers[w]
    if element % 3:
        0
    else:
        prime_numbers.pop(w)
    w += 1

w = 5
while w < len(prime_numbers):
    element = prime_numbers[w]
    if element % 5:
        0
    else:
        prime_numbers.pop(w)
    w += 1

w = 7
while w < len(prime_numbers):
    element = prime_numbers[w]
    if element % 7:
        0
    else:
        prime_numbers.pop(w)
    w += 1

print(prime_numbers)

