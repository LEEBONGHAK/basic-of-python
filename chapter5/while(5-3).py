# 5-3 while (반복문)

customer = "토르"
index = 5
while index >= 1:  # 어떤 조건이 만족 될 때까지 진행하라
    print("{0}, 커피가 준비 되었습니다. {1} 번 남았어요".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분되었습니다.")

'''
customer = "아이언맨"
index = 1
while True:
    print("{0}, 커피가 준비 되었습니다. 호출 {1}".format(customer, index))
    index += 1

무한 루프 - 종료를 위해 ctrl + c
무한 루프의 경우 최대한 사용하지 않는 편이 좋음 
'''
