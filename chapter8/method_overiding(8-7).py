# 8-7 메소드 오버라이딩
# 부모 클래스에서 정의된 메소드 말고, 자식 클래스에서 정의된 메소드를 사용하고 싶을때
# 메소드를 새롭게 정의해서 사용

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"
              .format(self.name, location, self.speed))


# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)  # Unit을 통해 이름과 체력을 받음
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]"
              .format(self.name, location, self.damage))

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
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"
              .format(name, location, self.flying_speed))


# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)  # 지상 유닛 speed 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 벌쳐 : 지상 유닛, 기동성 good
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루져 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)


# 매번 지상/공중 확인 후 각각의 맞는 함수 써야함
# 귀찮음 -> 메소드 오버로딩을 통해 한 함수만 쓸 수 있게 만들어 줌
vulture.move("11시")
battlecruiser.fly(battlecruiser.name, "9시")


# 이미 FlyableAttackUnit 속 move에 self.name을 던져 주기 때문에 location만 있어도 됨
battlecruiser.move("9시")
