# 6-5 가변 인자
def profile3(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    # end = " " : print문이 끝날때 줄바꿈을 하지 않고 띄어쓰기
    print(lang1, lang2, lang3, lang4, lang5)


profile3("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile3("김태호", 25, "Kotin", "Swift", "", "", "")
# 없는 부분을 써야하거나 추가하기 번거러움 -> 가변인자 사용


def profile4(name, age, *language):
    # end = " " : print문이 끝날때 줄바꿈을 하지 않고 띄어쓰기
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile4("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile4("김태호", 25, "Kotin", "Swift")
