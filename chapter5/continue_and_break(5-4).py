# 5-4 continue 와 break - 반복문 내에서 사용

absent = [2, 5]  # 결석
no_book = [7]  # 책을 안가져옴
for student in range(1, 11):  # 1 ~ 10번까지 존재
    if student in absent:
        continue  # 다음 반복을 진행
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break  # 다음 반복으로 진행하지 않고 탈출

    print("{0}야, 책을 읽어봐".format(student))
