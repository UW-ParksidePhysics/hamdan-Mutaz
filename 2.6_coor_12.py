n = int(input("What Value? "))
List1 = []

for i in range(0, n):

    List1.append(i+1)

    print(List1)

List2 = [j+1 for j in range(0, n)]

print(List2)
