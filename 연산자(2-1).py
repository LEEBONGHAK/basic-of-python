# 3-1 연산자

'''
+ : 덧셈
- : 뺄셈
* : 곱셈
/ : 나눗셈
** : 제곱 계산
% : 나머지 계산
// : 몫 계산
'''

print(1 + 1)  # 2
print(3 - 2)  # 1
print(5 * 2)  # 10
print(6 / 3)  # 2

print(2 ** 3)  # 제곱하기 2^3 = 8
print(5 % 3)  # 나머지 구하기 2
print(10 % 3)  # 1
print(5 // 3)  # 몫 구하기 1
print(10 // 3)  # 3

print(10 > 3)  # True
print(4 >= 7)  # Flase
print(10 < 3)  # Flase
print(5 <= 5)  # True

print(3 == 3)  # 앞뒤를 같은지 확인 True
print(4 == 2)  # Flase
print(3 + 4 == 7)  # True

print(1 != 3)  # 둘이 같지 않은지 확인 True
print(not(1 != 3))  # Flase

print((3 > 0) and (3 < 5))  # And 조건 True
print((3 > 0) & (3 < 5))  # And 조건의 다른 표현 True

print((3 > 0) or (3 > 5))  # Or 조건 True
print((3 > 0) | (3 > 5))  # Or 조건의 다른 표현 True

print(5 > 4 > 3)  # True
print(5 > 4 > 7)  # Flase
