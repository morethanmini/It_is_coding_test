n, m, k = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()

first = n_list[n-1]
second = n_list[n-2]

count = int(m / (k+1)) * k
count += m % (k+1)

result = 0
result += (count) * first
result += (m-count) * second

print(result)