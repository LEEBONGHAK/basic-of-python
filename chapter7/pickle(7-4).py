# 7-4 pickle
# 프로그램 상에서 우리가 사용하고 있는 데이터를 파일 형태로 저장

import pickle

'''
# b: 바이너리 타입 / pickle을 사용하기 위해 꼭 필요
profile_file = open("profil.pickle", "wb")
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
# profile 에 있는 정보를 file에 저장
pickle.dump(profile, profile_file)
profile_file.close()
'''

profile_file = open("profil.pickle", "rb")
# file에 있는 정보를 profile에 불러오기
profile = pickle.load(profile_file)
print(profile)
profile_file.close()
