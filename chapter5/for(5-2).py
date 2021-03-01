# 5-2 for (반복문)

for waiting_nu in [0, 1, 2, 3, 4]:
    print("대기번호 : {0}".format(waiting_nu))

for waiting_nu in range(5): # 0, 1, 2, 3, 4
    print("대기번호 : {0}".format(waiting_nu))

for waiting_nu in range(1, 6): # 1, 2, 3, 4, 5
    print("대기번호 : {0}".format(waiting_nu))

starbucks = ["아이언맨", "토르", "헐크"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))
