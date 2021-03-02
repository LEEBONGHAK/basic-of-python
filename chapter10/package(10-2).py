# 10-2 패키지(package)
# 모듈을 모아둔 집합 (폴더)

import travel.thailand
# import tarvel.thailand.ThailandPackage # 사용 불가
trp_to = travel.thailand.ThailandPackage()
trp_to.detail()
# 주의점 : import만 바로 사용 시 뒤에 모듈이나 패키지만 사용가능
# 함수 사용하고 싶으면 from ~ import ~ 구성 사용

from travel import vietnam
trp_to = vietnam.VietnamPackage()
trp_to.detail()