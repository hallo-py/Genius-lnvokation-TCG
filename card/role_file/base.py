import sys,os
sys.path.append(os.path.abspath(".\\..\\.."))

from Ruller import *
from Signal import *

element = {"pyro": 0,
           "hydro": 0,
           "anemo": 0,
           "electro": 0,
           "dendro": 0,
           "cryo": 0,
           "geo": 0,
           "color": 0,
           "uncolor": 0
           }

class base:
    name="base"    # 名字

    crystallize=0  # 护盾
    element_reactions=set() # 元素附着
    n_arms=None    # 现在装备的武器
    n_element=None # 现在的充能
    n_bonus=None   # 现在的圣遗物
    is_loading=False# 角色是否是上场角色

    # signal
    Hurt=signal()   # 掉血 slot(掉的血量)
    HpChange=signal() # 掉血 slot(掉到的血量)
    # fun
    def hurt(self,n):
        self.Hurt.emit(n)
        self.HpChange.emit(self.health-n)
        self.health-=n
    def addElement(self,elemen):
        self.element_reactions.append(element)
        self.emement_reactions=set(self.emement_reactions) # 去除重复
        self.emement_reactions=list(self.emement_reactions)

    health=0       # 血量
    vision=None    # 神之眼
    arms=None      # 武器类型
    max_element=2  # 元素充能最大值


    attack = None  # 普攻
    attack_e=element    # 需要的元素骰子

    skill = []     # 元素战技
    skill_e = []

    burst = []     # 元素爆发
    burst_e=[]

    nomal = []     # 被动技能

    '''
    def name(other):
        do something...
    '''
