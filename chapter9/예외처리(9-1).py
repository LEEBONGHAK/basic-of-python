# 9-1 예외처리 
# 어떤 에러 발생 시 그에 대해 처리를 해줌

'''
# try 내부 문장에서 오류 발생시 프로그램을 종료하지 않고
# except에 있는 문장 출력
try:
    print("나누기 전용 계산기 입니다.")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
'''


'''
# try 내부 문장에서 오류 발생시 프로그램을 종료하지 않고
# except에 있는 문장 출력
try:
    print("나누기 전용 계산기 입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1])) 까먹었다고 가정
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except: # 나머지 오류
    print("알 수 없는 에러가 발생하였습니다.") # 명시한 문장만 나타남
'''


try:
    print("나누기 전용 계산기 입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1])) 까먹었다고 가정
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err: # 어떤 에러인지 어떤 문장을 받고 싶다면
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)