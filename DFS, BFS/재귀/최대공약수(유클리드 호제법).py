"""
두 자연수 a, b에 대하여 (a>b) a를 b로 나눈 나머지를 r이라고 한다.
이때 a, b의 최대공약수는 b와 r의 최대공약수와 같다.
a, b의 최대공약수 = b, r의 최대공약수
"""

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(192, 162))