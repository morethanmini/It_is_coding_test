inp = input() # a1

row = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
col = [1, 2, 3, 4, 5, 6, 7, 8]

x = col[row.index(inp[0])] # a = 인덱스 0번, col[0] = 1
y = int(inp[1])
count = 0

move = [(-2, -1), (-1, -2),
        (-2, 1), (-1, 2),
        (1, -2), (2, -1),
        (1, 2), (2, 1)]

for go in move:
    nx = x + go[0]
    ny = y + go[1]

    if nx >= 1 and nx <= 8 and ny >= 1 and ny <=8:
        count += 1

print(count)