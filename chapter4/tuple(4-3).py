# 5-3 튜플 tuple ()
#  - 리스트와 다르게 내용 추가 및 변경 불가능 하지만 속도가 빠름

menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") - 오류남

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

(name, age, hobby) = ("김종국", 20 , "코딩") # 튜플을 이용해 한번에 지정 가능
print(name, age, hobby)
