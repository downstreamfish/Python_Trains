class Gun:

    def __init__(self, model):

        # 枪的型号
        self.model = model
        # 子弹数量
        self.bullet_count = 0

    def add_bullet(self, count):

        self.bullet_count += count

    def shoot(self):

        # 判断是否有子弹
        if self.bullet_count == 0:
            print("没有子弹了……")
            return
        # 发射一颗子弹
        print("%s 发射子弹[%d]" % (self.model, self.bullet_count))

        self.bullet_count -= 1


# 创建对象
ak47 = Gun('ak47')
ak47.add_bullet(50)
ak47.shoot()


class Soldier:

    def __init__(self, name):
        # 姓名
        self.name = name
        # 枪，士兵初始没有枪None 关键字表示什么都没有
        self.gun = None

    def fire(self):
        # 1. 判断士兵是否有枪
        if self.gun is None:
            print("[%s]还没有枪……" % self.name)
            return
        # 2. 高喊口号
        print("冲啊……[%s]" % self.name)

        # 3. 让枪装填子弹
        self.gun.add_bullet(50)

        # 4. 让枪发射子弹
        self.gun.shoot()

    # 给士兵配枪
    def add_gun(self, gun):
        if self.gun is None:
            self.gun = gun


soldier = Soldier('大头')
soldier.fire()
soldier.add_gun(ak47)
soldier.fire()
