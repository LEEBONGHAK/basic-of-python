# 1-4 변수
# 변수를 통해 해당 데이터를 쉽게 봐꿀 수 있다.
# 변수 : 값을 저장하는 공간

''' 애완동물을 소개하기'''
animal = "강아지"
name = "연탄이"
age = 4
hobby = "산책"
is_adult = age >= 3

print("우리집 " + animal + "의 이름은 " + name + "이에요")
print(name + "는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
print(f"{name}는 {age}살이며, {hobby}을 아주 좋아해요")
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
# ',' 로 나타낼 수 있으나 중간에 빈칸이 추가됨

print(name + "는 어른일까요? " + str(is_adult))
