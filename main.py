n = [1, 2, 3, 4, 5]
lost = [2, 4]
result = []

for i in n:
    if i not in lost:
        result.append(i)

result1 = [i for i in n if i not in lost]

print(result)
print(result1)