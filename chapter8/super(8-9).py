# 8-9 super


# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(
            self.name, location, self.speed))


# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)  # Unit을 통해 이름과 체력을 받음
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(
            self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))


# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(
            name, location, self.flying_speed))


# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 유닛 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        # super()를 통해 초기화 가능 이때는 self를 쓰지 않음
        super().__init__(name, hp, 0)
        self.location = location


'''
super()의 문제점
class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        super().__init__()

class FlyableUnit1(Flyable, Unit):
    def __init__(self):
        super().__init__()


# 드랍쉽
dropship = FlyableUnit() # Unit 생성자
dropship1 = FlyableUnit1() # Flyable 생성자

'''2개 이상의 다중 상속을 쓰는 경우 super() 를 쓰면 순서상 맨 "처음"
클래스에 대해서 __init__ 함수가 호출 됨'''

class FlyableUnit2(Flyable, Unit):
    def __init__(self):
        # super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

dropship2 = FlyableUnit2()

'''이러한 문제가 있기 때문에 단독 상속 및 모든 부모 클래스에 대해 필요하다면
super() 를 사용하지 않고 모두 명시하여 초기화 시켜주어야 한다.'''

'''
