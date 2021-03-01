# 10-3 사용자 정의 예외처리
# 사용자가 직접 에러를 정의하여 사용할 수 있음
# class로 에러를 정의하여 사용

class BigNumberError(Exception):
    # 에러가 발생했을 때 메세지를 넣고 싶다면
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):  # str = string
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
