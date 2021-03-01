# 8-2 __init__
# __init__ : 파이썬에서 쓰이는 생성자

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))


marine1 = Unit("마린", 40, 5) # Unit class의 인스턴스
marine2 = Unit("마린", 40, 5) # Unit class의 인스턴스
tank1 = Unit("탱크", 150, 35) # Unit class의 인스턴스


# Unit에 정의된 객체 만큼 없기 때문에
# marine3 = Unit("마린") # 사용불가
# marine4 = Unit(40) # 사용불가
