# 10-5 패키지, 모듈 위치
# inspect.getabsfile('패키지명 or 모듈명') : 패키지 및 모듈 위치 확인

from travel import thailand
import inspect
import random


print(inspect.getabsfile(random))
print(inspect.getabsfile(thailand))
