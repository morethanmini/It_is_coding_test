# N, M 을 공백으로 구분하여 입력 받기
n, m = map(int, input().split())

# 방문할 위치를 저장할 배열 선언
check = [[0]*m for _ in range(n)]
# 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력 받기
A, B, d = map(int, input().split())
# 시작 위치는 방문 선언
check[A][B] = 1

# 전체 맵 정보 입력 받기
map_status = []
for i in range(n):
    row = list(map(int, input().split()))
    map_status.append(row)

# 북, 동, 남, 서 방향 선언
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# 왼쪽으로 회전하는 함수
def left_turn():
    global d
    d += 1
    if (d == 4):
        d = 0

# 방문한 칸의 수 (시작 위치는 방문한 것으로 설정)
count = 1
# 각 좌표별 회전한 횟수
turn_time = 0
while True:

    # 왼쪽으로 회전
    left_turn()
    # 바라보는 방향의 좌표
    nx = A + dx[d]
    ny = B + dy[d]
    # 바라보는 방향이 맵 내부에 있는지 확인
    if (nx >= 0 and nx < n and ny >= 0 and ny < m):
        # 해당 방향으로 방문할 수 있는지 확인
        if (check[nx][ny] == 0 and map_status[nx][ny] == 0):
            # 현재 위치 변경
            A = nx
            B = ny
            # 방문 체크
            check[nx][ny] = 1
            # 방문 칸수 추가
            count += 1
            # 회전 횟수 초기화
            turn_time = 0
            continue
        # 해당 방향으로 방문할 수 없다면
        else:
            turn_time += 1
        # 회전 횟수가 찼다면
        if (turn_time == 4):
            # 바라보는 방향은 그대로 두고, 위치만 뒤로 변경
            nx = A - dx[d]
            ny = A - dy[d]
            # 뒤로 갈 수 있다면
            if (check[nx][ny] == 0 and map_status[nx][ny] == 0):
                A = nx
                B = ny
                # 회전 횟수 초기화
                turn_time = 0
            # 뒤로 갈 수 없다면
            else:
                break

print(count)
