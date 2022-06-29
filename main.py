#예제 4-2 시각
n = int(input())
count = 0

for h in range(n+1): # 시
    for m in range(60): # 분
        for s in range(60): # 초
            # 3이 있는지 확인
            if '3' in str(h) + str(m) + str(s):
                count += 1

print(count)
