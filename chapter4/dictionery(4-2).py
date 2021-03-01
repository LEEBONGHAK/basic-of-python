# 5-2 사전 {'키':'해당값'}

cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))  # 값을 가져오는 다른 방법
# print(cabinet[5]) # 5에 해당하는 값이 없기 때문에 오류
print(cabinet.get(5))  # 값이 없으면 none으로 반환 후 프로그램 계속
print(cabinet.get(5, "사용 가능"))  # none 대신 다른 지정 값으로 나타나게 만듬

print(3 in cabinet)  # True / 3이 cabinet에 있는지 확인(불리언)
print(5 in cabinet)  # Flase

cabinet = {"A-3": "유재석", "B-100": "김태호"}
print(cabinet["A-3"])  # 유재석
print(cabinet["B-100"])  # 김태호

# 새롭게 키 지정
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"  # C-20 에 조세호 지정 / 값이 이미 있을 경우 값이 업데이트 됨
print(cabinet)

# 지정 키 삭제
del cabinet["A-3"]
print(cabinet)

# 키 들만 출력
print(cabinet.keys())  # dict_keys(['B-100', 'C-20'])

# 값들만 출력
print(cabinet.values())  # dict_values(['김태호', '조세호'])

# 키, 값 쌍으로 출력
print(cabinet.items())  # dict_items([('B-100', '김태호'), ('C-20', '조세호')])

# 지정 키 모두 삭제
cabinet.clear()
print(cabinet)  # {}
