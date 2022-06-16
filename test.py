arr = list(input().split())
arr_int =list(map(int, arr))

arr_int.sort()
arr_len = len(arr)
lr = []

for i in range(1, arr_len+1):
    lr.append(i)

if arr_int == lr:
    print(True)
else:
    print(False)

def solution(arr):
    arr_int = list(map(int, arr))
    arr_int.sort()
    arr_len = len(arr_int)
    lr = []

    for i in range(1, arr_len+1):
        lr.append(i)

    if arr_int == lr:
        return True
    else:
        return False

print(solution([4,1,3,2]))