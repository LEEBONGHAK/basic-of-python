# 4-1 리스트 [] - 순서를 가지는 객체의 집합

# 지하철 칸별로 10명, 20명, 30명
subway = [10, 20, 30]
print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

# 조세호씨가 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))  # 1

# 하하씨가 다음 정류장에서 다음 칸에 탐
# .append() : 맨 뒤에 더해줌
subway.append("하하")
print(subway)  # ["유재석", "조세호", "박명수", "하하"]

# 정형돈씨를 유재석 / 조세호 사이에 태워봄
# .insert() 해당하는 위치에 넣어줌
subway.insert(1, "정형돈")
print(subway)  # ["유재석", "정형돈", "조세호", "박명수", "하하"]

# 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# .pop() : 뒤에서 순서대로 뺌
print(subway.pop())
print(subway)  # ["유재석", "정형돈", "조세호", "박명수"]

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("하하")
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬하기
num_list = [5, 4, 3, 2, 1]
# .sort() : 리스트 정렬
num_list.sort()
print(num_list)  # [1, 2, 3, 4, 5]

# 순서 뒤집기 기능
num_list.reverse()
print(num_list)  # [5, 4, 3, 2, 1]

# 모두 지우기
num_list.clear()
print(num_list)  # []

# 리스트는 자료형에 구애받지 않고 다양한 자료형과 함께 사용가능
num_list = [5, 4, 3, 2, 1]
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)  # 리스트 합치기
print(num_list)  # [5, 4, 3, 2, 1, "조세호", 20, True]
