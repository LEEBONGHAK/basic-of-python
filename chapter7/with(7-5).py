# 8-5 with 
# 파일 입출력의 다른 방법 (pickle도 사용가능)

import pickle

# 파일을 열어 변수에 저장
with open("profil.pickle", "rb") as profile_file: 
    # load를 통해 불러옴
    print(pickle.load(profile_file))
    # close() 사용할 필요 없음

'''with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요")'''

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())
