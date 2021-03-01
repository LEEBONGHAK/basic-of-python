# 7-6 지역변수와 전역변수
# 지역변수 : 함수 내에서만 사용가능한 변수
# 전역변수 : 프로그램 전체에서 사용가능한 변수

gun = 10

# def checkpoint(soldiers): # 경계근무
#     gun = 20 # 함수 내에서 변수를 따로 지정해 줘야함(지역변수)
#     gun = gun - soldiers
#     print("[함수내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))    - 10
# checkpoint(2) # 2 명이 경계근무 나감  - 18
# print("남은 총 : {0}".format(gun))    - 10


def checkpoint(soldiers):  # 경계근무
    global gun  # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수내] 남은 총 : {0}".format(gun))


print("전체 총 : {0}".format(gun))
checkpoint(2)  # 2 명이 경계근무 나감
print("남은 총 : {0}".format(gun))
# 전역 변수를 많이 쓰면 프로그램 관리가 힘들어짐;;


def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수내] 남은 총 : {0}".format(gun))
    return gun  # 지역변수의 값을 밖으로 던질 수 있음


print("전체 총 : {0}".format(gun))
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))
