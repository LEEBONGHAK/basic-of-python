# 9-4 finally
# 예외 처리 구문 중 에러 발생 상관없이 '무조건' 실행됨

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        # raise를 통해 에러를 만들어 낼 수 있음
        raise BigNumberError("입력 값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
    print(err)
# 에러가 발생해도 강제 종료를 막으므로써 완성도를 높인다!!
finally:
    print("계산기를 이용해 주셔서 감사합니다.")
