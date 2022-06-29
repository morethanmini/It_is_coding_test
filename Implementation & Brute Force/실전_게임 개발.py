# 실전3 게임 개발

# 입력
N, M = map(int, input().split())  # 세로 x 가로
A, B, d = map(int, input().split())  # 위치, 바라보는 방향
maps = [[i for i in map(int, input().split())] for n in range(N)]  # 지도
visited = [[0] * M for n in range(N)]  # 방문 배열
visited[A][B] = 1

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global d
    d = d - 1
    if d == -1:
        d = 3

# 시뮬레이션 시작
cnt = 1
turn_time = 0
while True:
    turn_left()
    a = A + dx[d]
    b = B + dy[d]

    if visited[a][b] == 0 and maps[a][b] == 0:
        visited[a][b] = 1
        A = a
        B = b
        cnt += 1
        turn_time = 0
        continue
    else:
        turn_time += 1

    if turn_time == 4:
        a = A - dx[d]
        b = B - dy[d]
        if maps[a][b] == 0:
            A = a
            B = b
        else:
            break
        turn_time = 0

print(cnt)