# 11-1 모듈(module)
# 필요한 것들끼리 부품처럼 잘 만들어진 파일
# 코드의 유지 보수가 쉬워짐
# 모듈 : 파이썬에선 class나 def 등을 포함하고 있는 파일 (확장자 : .py)
# 모듈을 그 모듈을 쓰려는 파일이 같은 경로에 있거나 파이썬 라이브러리가 모여있는 파일에 존재 해야함

'''
import theater_module
theater_module.price(3)
# 3명이서 영화 보러 갔을 때 가격

theater_module.price_mornig(4)
# 4명이서 조조 영화 보러 갔을 때 가격

theater_module.price_soldier(5)
# 군인 5명이서 영화 보러 갔을 때 가격
'''

'''
import theater_module as mv 
# theater_module을 mv로 별명을 붙여주어 모듈명을 줄여서 사용가능

mv.price(3)
mv.price_mornig(4)
mv.price_soldier(5)
'''

'''
from theater_module import *
# theater_module 필요없이 모든 것을 사용하겠다.

price(3)
price_mornig(4)
price_soldier(5)
'''

'''
from theater_module import price, price_mornig
# 선택적으로 가져올 수 도 있다.

price(3)
price_mornig(4)
# price_soldier(5) : 가져오지 않았기 때문에 오류남
'''

# 하나만 가져올 경우 별명을 붙여 사용 가능
from theater_module import price_soldier as price
price(5)
