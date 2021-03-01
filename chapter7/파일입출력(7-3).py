# 7-3 파일 입출력

'''
# 파일 열고, 목적(w : 덮어 쓰기), utf8(한글 정보를 잘 쓰기 위함)
score_file = open("score.txt", "w", encoding="utf8")
print("수학 : 0", file = score_file)
print("영어 : 50", file = score_file)
score_file.close() # 닫아주기
'''

'''
# a : 이어쓰기
score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80") # 파일에 쓰는 다른 방법
score_file.write("\n코딩 : 100") # 이걸 쓸 경우 줄바꿈이 포함되지 않아있음
score_file.close()
'''

'''
# r : 읽기
score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read()) # 파일에 있는 모든 내용 읽기
score_file.close()
'''

'''
score_file = open("score.txt", "r", encoding="utf8")
# 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end = "")
print(score_file.readline(), end = "")
print(score_file.readline(), end = "")
print(score_file.readline(), end = "")
score_file.close()
'''

'''
# 몇 줄인지 모를때
score_file = open("score.txt", "r", encoding="utf8") 
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end = "")
score_file.close()
'''

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines()
# 모든 줄을 list 형태로 저장
for line in lines:
    print(line, end="")
score_file.close()
print("\n")
