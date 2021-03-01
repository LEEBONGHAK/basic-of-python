# 5-4 집합(set)
# 중복이 안되고 순서가 없음

my_set = {1, 2, 3, 3, 3}
# set의 특성으로 인해 3은 한번만 나옴
print(my_set)  # {1, 2, 3}

java = {"유재석", "김태호", "양세형"}
# set([]) - set으로 정의 가능
python = set(["유재석", "박명수"])

# 교집합 (java 와 python 을 모두 할 수 있는 개발자)
print(java & python)  # {'유재석'}
print(java.intersection(python))  # {'유재석'}

# 합집합 (java 할 수 있거나 python  할 수 있는 개발자)
print(java | python)  # {'유재석', '박명수', '양세형', '김태호'}
print(java.union(python))  # {'유재석', '박명수', '양세형', '김태호'}

# 차집합 (java 는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)  # {'양세형', '김태호'}
print(java.difference(python))  # {'양세형', '김태호'}

# python 할 줄 하는 사람이 늘어남 (추가)
python.add("김태호")
print(python)  # {'유재석', '박명수', '김태호'}

# java 를 할 줄 모름 (제외)
java.remove("김태호")
print(java)  # {'유재석', '양세형'}
