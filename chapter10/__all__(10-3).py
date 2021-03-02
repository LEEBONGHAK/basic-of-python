# 10-3 __all__

from travel import *

trp_to = vietnam.VietnamPackage()
trp_to.detail()

trp_to_2 = thailand.ThailandPackage()
trp_to_2.detail()  # 오류 (thailand 모듈이 공개되어 있지 않아서)

# * 는 모든것을 가져오겠다는 뜻이지만 실제로는 공개범위 설정해줘야함
# 이것을 해결해 주기 위해 __init__.py에 __all__에 모듈 이름을 추가하여야 한다. (즉, 공개해주는 것)
