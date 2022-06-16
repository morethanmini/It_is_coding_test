import math

a = 21
b = 14

def lcm(a, b): # 최소 공배수 함수
    return a * b // math.gcd(a, b) # 최소 공배수 : 두 수의 곱을 최대공약수로 나눔

print(math.gcd(a,b)) # 최대 공약수 출력
print(lcm(a, b)) # 최소 공배수 출력
