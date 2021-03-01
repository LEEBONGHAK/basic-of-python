# 2-4 랜덤함수
from random import *  # 랜덤 라이브러리 불러오기

print(random())  # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10)  # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10))  # 0 ~ 10 미만의 임의의 값 생성 / int() : 정수값 부분만 볼 수 있게 해줌
print(int(random() * 10) + 1)  # 1 ~ 10 이하의 임의의 값 생성

# 로또 숫자를 뽑기
print(int(random() * 45) + 1)  # 1 ~ 45 이하의 임의의 값 생성
print(randrange(1, 46))  # 1 ~ 46 미만의 임의의 값 생성 (정수값)
print(randint(1, 45))  # 1 ~ 45 이하의 임의의 값 생성 (정수값)
