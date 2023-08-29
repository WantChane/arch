def DirectAddtion(list):
    result = 0
    try:
        for i in list:
            result += i
    except TypeError:
        pass
    return result


def DirectMultiplication(list):
    result = 1
    try:
        for i in list:
            result += i
    except TypeError:
        pass
    return result


def FinalAddtion(list):
    result = 0
    try:
        for i in list:
            result += i
    except TypeError:
        pass
    return result


def FinalMultiplication(list):
    result = 1
    try:
        for i in list:
            result *= i
    except TypeError:
        pass
    return result

def atkd_add(list):
    result = 100
    try:
        for i in list:
            result+=i
            if result>600:
                result = 600
            if result<20:
                result = 20
    except TypeError:
        pass
    return result

class Cal(object):
    def __init__(self, item) -> None:
        self.item = item
        self.DA_list = []
        self.DM_list = []
        self.FA_list = []
        self.FM_list = []

    def addDA(self, i):
        self.DA_list.append(i)

    def addDM(self, i):
        self.DM_list.append(i)

    def addFA(self, i):
        self.FA_list.append(i)

    def addFM(self, i):
        self.FM_list.append(i)

    def get(self):
        return round(((self.item + DirectAddtion(self.DA_list))*DirectMultiplication(self.DM_list)+FinalAddtion(self.FA_list))*FinalMultiplication(self.FM_list))


if __name__ == "__main__":

    # 银灰 攻击
    SilverAsh_atk = Cal(717)
    SilverAsh_atk.addDM(0.1)  # 银灰天赋
    SilverAsh_atk.addDM(2)  # 真银斩
    # atk.addDM(0.9)#ff0
    SilverAsh_atk.addFA(443*0.6)  # 2903 红蒂2
    print('2903红蒂+2603银灰真银斩dph', SilverAsh_atk.get())

    # 2903星熊 防御
    Hoshihguma_def = Cal(783)
    Hoshihguma_def.addDA(140)  # x模组
    Hoshihguma_def.addDM(0.06)  # 在场
    Hoshihguma_def.addDM(0.11)  # 在场
    Hoshihguma_def.addDM(0.3)  # 2技能
    Hoshihguma_def.addDM(0.2)  # 阻挡
    print('2903x模2技能阻挡星熊def', Hoshihguma_def.get())
    
    #失控狂暴宿主组长 攻击力
    enemy01_atk = Cal(1750)
    enemy01_atk.addFM(1.15**5)#N15 5层
    enemy01_atk.addFM(1.2)#紧急
    enemy01_atk.addFM(1.2)#N15精英怪
    print('n15紧急失控1750哥atk',enemy01_atk.get())
    
    enemy01_hp = Cal(30000)
    enemy01_hp.addFM(1.15**5)
    enemy01_hp.addFM(1.2)#n11
    enemy01_hp.addFM(1.2)#n15
    enemy01_hp.addFM(1.5)#紧急

    print('n15紧急失控1750哥hp',enemy01_hp.get())
    
    
    #思维折断
    baopoatk = Cal(2200)
    baopoatk.addFM(1.16**3)#N15 3层
    baopoatk.addFM(1.1)#N4 精英怪
    baopoatk.addFM(1.1)#N0 怪
    baopoatk.addFM(1.1)#N15 怪
    baopoatk.addFM(1.1)#紧急
    baopoatk.addFM(1.05)#N5 怪
    
    print('N15紧急思维折断爆破锤atk',baopoatk.get())



