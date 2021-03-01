# 3-4 문자열 포맷

print("a" + "b")  # ab
print("a", "b")  # a b

# 방법 1 %d %s %c 사용
print("나는 %d살입니다." % 20)  # %d 정수값 / 뒤에 있는 숫자를 반환
print("나는 %s을 좋아해요" % "파이썬")  # %s 문자열
print("Apple은 %c로 시작해요." % "A")  # %c 한 글자 반환

print("나는 %s살입니다." % 20)
print("나는 %s색과 %s색을 좋아해요" % ("파란", "빨간"))

# 방법 2 .format() 사용
print("나는 {}살입니다.".format(20))
print("나는 {}색과 {}색을 좋아해요" .format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요" .format("파란", "빨간"))  # 포맷 뒤의 넣고 싶은 것를 지정해 줄 수 있다.
print("나는 {1}색과 {0}색을 좋아해요" .format("파란", "빨간"))

# 방법 3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨강"))
# .format()에서 지정한 변수를 넣어 사용할 수 있다.
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨강", age=20))

# 방법 4 (v 3.6 이상~)
age = 20
color = "빨간"
# f를 사용하여 문장을 쓰면 실제 변수에서 사용한 값을 그대로 사용 가능
print(f"나는 {age}살이며, {color}색을 좋아해요.")
