# 7-1 표준 입출력

print("Python", "Java")  # Python Java
print("Python" + "Java")  # PythonJava

# sep = 를 통해 띄어 쓰기를 할지 다른 걸 할지 지정 가능
print("Python", "Java", sep=", ")  # Python, Java
print("Python", "Java", sep=" vs ")  # Python vs Java

# end = 를 통해 줄 바꿈을 하지 않고 이어서 쓸 수 있음
print("Python", "Java", sep=", ", end="?")
print("무엇이 더 재밌을까요?")
# Python, Java?무엇이 더 재밌을까요?

# 표준 출력으로 처리
print("Python", "Java", file=sys.stdout)
# 표준 에러로 처리
print("Python", "Java", file=sys.stderr)
# 로그 처리 시 표준 출력 시 잘 출력되는 부분 (상관 x) , 표준 에러 - 따로 에러처리 가능


scores = {"수학": 0, "영어": 50, "코딩": 100}
for subject, score in scores.items():
    print(subject, score)

for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")
# .ljust(num) num만큼 공간 확보를 하고 왼쪽 정렬
# .rjust(num) num만큼 공간 확보를 하고 오른쪽 정렬


# 은행 대기 순번표
# 001, 002, 003, ...
for num in range(1, 21):
    print("대기번호 : " + str(num).zfill(3))
# .zfill(num) num만큼 공간을 확보하고 값이 없는 곳은 0으로 채움


answer = input("아무 값이나 입력하세요 : ")  # str으로 받음 (문자열로)
print("입력하신 값은 " + answer + "입니다.")
