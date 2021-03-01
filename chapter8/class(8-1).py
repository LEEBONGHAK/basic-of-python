# 8-1 클래스(class)
# 스타크래프트 예로 들 것임

# 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
name = "마린"  # 유닛 이름
hp = 40  # 유닛 체력
damage = 5  # 유닛 공격력

print("{} 유닛이 생성되었습니다.".format(name))
print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# 탱크 : 공격 유닛, 탱크, 포 사용, 일반 / 시즈 모드
tank_name = "탱크"
tank_hp = 150
tank_damage = 35

print("{} 유닛이 생성되었습니다.".format(tank_name))
print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))

tank2_name = "탱크"
tank2_hp = 150
tank2_damage = 35

print("{} 유닛이 생성되었습니다.".format(tank2_name))
print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))


def attack(name, location, damage):
    print(" {0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".
          format(name, location, damage))


attack(name, "1시", damage)
attack(tank_name, "1시", tank_damage)
attack(tank2_name, "1시", tank2_damage)
print("\n")


# 매번 적어주기 번거러움 -> 클래스 사용
# 클래스는 붕어빵 틀로 비유 / 연관있는 변수와 함수의 집합
# 위의 것을 클래스로 만들어서 사용


# 일반 유닛
class Unit:
    # __init__을 통해 필요한 값 정의해줌
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}\n".format(self.hp, self.damage))


marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank1 = Unit("탱크", 150, 35)
