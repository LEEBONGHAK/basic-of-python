# 5-5 자료 구조의 변경

menu = {"커피", "우유", "주스"}

# type() : 자료 구조 판별해서 알려줌
print(type(menu))  # <class 'set'>

menu = list(menu)
print(type(menu))  # <class 'list'>

menu = tuple(menu)
print(type(menu))  # <class 'tuple'>

menu = set(menu)
print(type(menu))  # <class 'set'>
