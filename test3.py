import sys
n = sys.stdin.readline()

arr1 = [[1,2], [2,3]]
arr2 = [[4,5], [6,7]]

answer = arr1

for i in range(len(arr1)):
    for j in range(len(arr1[i])):
        answer[i][j] = arr1[i][j] + arr2[i][j]

print(answer)
