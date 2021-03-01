# 3-3 문자열 처리 함수

python = "Python is Amazing"

print(python.lower())  # 문자열.lower() : 모든 문자 소문자로
print(python.upper())  # 문자열.upper() : 모든 문자 대문자로
print(python.capitalize())  # 문자열.capitalize() : 문자열의 첫글자만 대문자로
print(python[0].isupper())  # 문자열의 []번째가 대문자인지 판단하여 반환
print(len(python))  # 문자열의 길이를 반환
print(python.replace("Python", "Java"))  # 문자열을 찾아 대체

index = python.index("n")  # index로 지정된 문자가 어디에 있는지 반환
print(index)
index = python.index("n", index + 1)  # index(지정문자, 시작점)
print(index)

# index와 비슷하지만 원하는 문자가 포함되어 있지 않은 경우 -1 반환(index의 경우 오류남)
print(python.find("n"))
print(python.find("Java"))

print(python.count("n"))  # 원하는 문자가 몇 번 나왔는지 반환
