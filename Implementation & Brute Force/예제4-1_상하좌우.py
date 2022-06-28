# 상하좌우
n = int(input())
x, y = 1, 1
move = input().split() # 움직이는 방향 순서대로 입력

# L R U D 이동 좌표
dx = [0, 0, -1, 1]
dy = [-1, 1, 0 ,0]
move_type = ['L', 'R', 'U', 'D']

for i in move: # 움직이는 방향 순서 포문 ex) R R R U D D
    for j in range(len(move_type)): # L R U D(4) : 0 1 2 3
        if i == move_type[j]:
            nx = x + dx[j] # 현재 x좌표 + x이동 좌표
            ny = y + dy[j] # 현재 y좌표 + y이동 좌표

    # 좌표에서 벗어나는 경우
    if nx < 1 or ny <1 or nx > n or ny > n:
        continue

    x, y = nx, ny

print(x, y)
