from base import *

class ganyv(base):
    name="甘雨"    # 名字

    health=10       # 血量
    vision=cryo    # 神之眼
    arms=bow      # 武器类型
    max_element=3  # 元素充能最大值

    def attacked(self,other):
        other.hurt(2)
    attack = attacked  # 普攻
    attack_e=element
    attack_e["cryo"]=1;attack_e["uncolor"]=2

    
    skill = []     # 元素战技
    skill_e = []

    burst = []     # 元素爆发
    burst_e = []

    nomal = []     # 被动技能


a=ganyv()
b=ganyv()

a.health=10
b.health=10

def h(a):
    print(a)
b.HpChange.connect(h)
a.attack(b)
