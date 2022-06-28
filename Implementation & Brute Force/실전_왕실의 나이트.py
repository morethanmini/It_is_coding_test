# 왕실의 나이트

location = input() # 현재 좌표 입력 ex) a1
x = int(ord(location[0])) - int(ord('a')) + 1 # a
y = int(location[1]) # 1

move = [(-2, -1), (-1, -2),
        (1, -2), (2, -1),
        (2, 1), (1, 2),
        (-1, 2), (-2, 1)] # 이동 가능한 좌표

count = 0

for i in move:
    nx = x + i[0]
    ny = y + i[1]

    if nx >= 1 and nx <= 8 and ny >= 1 and ny <= 8:
        count += 1

print(count)
