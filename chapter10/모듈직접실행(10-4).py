# 10-4 모듈 직접 실행
# 패키지나 모듈이 잘 작동하는 지 테스트 하는 방법

'''
ex) thailand.py 에서
if __name__ == "__main__":
    print("Tailand 모듈 직접 실행")
    print("이 문장은 모듈을 직접 실행할 때만 실행돼요")
    trip_to = ThailandPackage()
    trip_to.detail()
else:
    print("Thailand 외부에서 모듈 호출")

을 작성하고 직접 실행하면 모듈 구문과 if문이 실행 모듈로 사용되면 모듈 구문과 else문 실행
'''
