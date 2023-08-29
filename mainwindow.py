from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView
from Ui_mainwindow import Ui_MainWindow
from ExtendedComboBox import *
from Calculate import *
import json


def getData(path):
    try:
        with open(r'info\{}.json'.format(path), 'r', encoding='utf-8-sig') as file:
            f = file.read()
            return json.loads(f)
    except FileNotFoundError:
        return ''


def getConfig():
    try:
        with open(r'config\config.json', 'r', encoding='utf-8-sig') as file:
            f = file.read()
            return json.loads(f)
    except FileNotFoundError:
        return ''


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # region 初始信息
        self.Mission_name.setText("你好 集批!")

        self.Theme_ch.setCurrentIndex(-1)
        self.Theme_ch.lineEdit().setPlaceholderText("请选择主题:")
        self.Difficulty_ch.setCurrentIndex(-1)
        self.Difficulty_ch.lineEdit().setPlaceholderText("请选择难度:")
        self.Mission_ch.setCurrentIndex(-1)
        self.Mission_ch.lineEdit().setPlaceholderText("请选择关卡:")
        self.Floor_ch.setCurrentIndex(-1)
        self.Floor_ch.lineEdit().setPlaceholderText("请选择层数:")

        config = getConfig()

        self.ene_name.setChecked(config["enemylist_name"])
        self.setEnemylistCol(self.ene_name)
        self.ene_count.setChecked(config["enemylist_count"])
        self.setEnemylistCol(self.ene_count)
        self.ene_status.setChecked(config["enemylist_status"])
        self.setEnemylistCol(self.ene_status)
        self.ene_level.setChecked(config["enemylist_level"])
        self.setEnemylistCol(self.ene_level)
        self.ene_hp.setChecked(config["enemylist_hp"])
        self.setEnemylistCol(self.ene_hp)
        self.ene_atk.setChecked(config["enemylist_atk"])
        self.setEnemylistCol(self.ene_atk)
        self.ene_def.setChecked(config["enemylist_def"])
        self.setEnemylistCol(self.ene_def)
        self.ene_res.setChecked(config["enemylist_res"])
        self.setEnemylistCol(self.ene_res)
        self.ene_atkd.setChecked(config["enemylist_atkd"])
        self.setEnemylistCol(self.ene_atkd)
        self.ene_weight.setChecked(config["enemylist_weight"])
        self.setEnemylistCol(self.ene_weight)
        self.ene_speed.setChecked(config["enemylist_speed"])
        self.setEnemylistCol(self.ene_speed)
        self.ene_atkr.setChecked(config["enemylist_atkr"])
        self.setEnemylistCol(self.ene_atkr)
        self.ene_deb.setChecked(config["enemylist_deb"])
        self.setEnemylistCol(self.ene_deb)

        # endregion
        # region 信号与槽
        self.Theme_ch.currentTextChanged.connect(self.themeChanged)
        # self.Difficulty_ch.currentTextChanged.connect(self.difficultyChanged)
        self.Mission_ch.currentTextChanged.connect(self.missionChanged)
        self.Confirm.clicked.connect(self.ConfirmClick)
        # endregion
        # region 敌人表格初始化
        self.Enemy_list.verticalHeader().setVisible(False)  # 隐藏垂直表头
        self.Enemy_list.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.Enemy_list.horizontalHeader().setSectionResizeMode(
            0, QHeaderView.ResizeToContents)  # 自动分配列宽

        # endregion
        # region 可视化菜单栏
        self.ene_name.toggled.connect(
            lambda: self.setEnemylistCol(self.ene_name))
        self.ene_count.toggled.connect(
            lambda: self.setEnemylistCol(self.ene_count))
        self.ene_status.toggled.connect(
            lambda: self.setEnemylistCol(self.ene_status))
        self.ene_level.toggled.connect(
            lambda: self.setEnemylistCol(self.ene_level))
        self.ene_hp.toggled.connect(
            lambda: self.setEnemylistCol(self.ene_hp))
        self.ene_atk.toggled.connect(
            lambda: self.setEnemylistCol(self.ene_atk))
        self.ene_def.toggled.connect(
            lambda: self.setEnemylistCol(self.ene_def))
        self.ene_res.toggled.connect(
            lambda: self.setEnemylistCol(self.ene_res))
        self.ene_atkd.toggled.connect(
            lambda: self.setEnemylistCol(self.ene_atkd))
        self.ene_weight.toggled.connect(
            lambda: self.setEnemylistCol(self.ene_weight))
        self.ene_speed.toggled.connect(
            lambda: self.setEnemylistCol(self.ene_speed))
        self.ene_atkr.toggled.connect(
            lambda: self.setEnemylistCol(self.ene_atkr))
        self.ene_deb.toggled.connect(
            lambda: self.setEnemylistCol(self.ene_deb))
        self.ene_s1.toggled.connect(lambda: self.setEnemylistRow(self.ene_s1))
        self.ene_s2.toggled.connect(lambda: self.setEnemylistRow(self.ene_s2))
        self.ene_s3.toggled.connect(lambda: self.setEnemylistRow(self.ene_s3))
        # endregion
    # region 函数定义

    def themeChanged(self, theme):
        self.Mission_ch.clear()
        self.Difficulty_ch.clear()
        self.Floor_ch.clear()
        self.Mission_name.setText("你好 集批!")
        self.Blood_display.setText("")
        self.Enemy_count_display.setText("")
        self.Min_time_display.setText("")
        self.Place_display.setText("")
        self.Cost_display.setText("")
        self.Max_cost_display.setText("")
        self.Detail_display.setText("")
        self.Place_display.setText("")
        self.Cost_display.setText("")
        self.Max_cost_display.setText("")
        self.Detail_display.setText("")
        self.Enemy_list.setRowCount(0)

        config = getConfig()
        if theme == '傀影与猩红孤钻':
            self.Mission_ch.addItems(['与虫为伴', '驯兽小屋', '礼炮小队', '意外', '死斗', '压轴登场', '巡逻队', '落魄骑士', '分赃不均', '先来后到', '正义', '似曾相识', '酒商运输队', '从众效应', '斗兽笼', '首演', '感化', '雕匠与石像', '步步紧逼', '阴云笼罩', '烟花秀', '永无尽头', '远方来客', '共舞', '鲍勃酒品', '雪山上的来客', '无人机起降库',
                                     '红雾弥漫', '仪式之夜', '彻骨冰寒', '危机四伏', '惊喜工厂', '荒唐把戏', '隔岸观火', '萨卡兹的渴求', '乌萨斯的渴求', '开门请当心', '大盗当头', '恐怖传说', '悦耳杀机', '寒渊惜别', '覆水难收', '别无所求', '诸事不顺', '再启新篇', '鸭爵的戏剧', '鸭爵的宴会', '高普尼克之拳', '这位乌萨斯人', '“骑士对决”', '邪异囚笼', '无序盛宴', '自缚', '观察'])
            self.Difficulty_ch.addItems(['古堡观光', '正式调查', '直面灾厄'])
            self.Difficulty_ch.setCurrentIndex(
                config["theme_2_startdifficuilt"])
        elif theme == '水月与深蓝之树':
            self.Mission_ch.addItems(['蓄水池', '虫群横行', '射手部队', '共生', '互助', '无声呼号', '海神的信者', '病症', '征兆', '除暴安良', '回溯', '饥渴', '原始部落', '精酿杀手', '据险固守', '巢穴', '漩涡', '大君遗脉', '瞻前顾后', '地下天途', '火之骄子', '领地意识', '海窟沙暴', '溟痕乐园', '狩猎场', '崇敬深海', '铳与秩序', '机械之灾', '教徒居所', '失控',
                                     '吹笛人的号召', '好梦在何方', '育生池', '蔓延', '余烬方阵', '水火相容', '深度认知', '永恒安息', '分离与统一', '纠错', '永恒愤怒', '异体同心', '订正', '认知即重担', '“命运的宠儿”', '大群所向', '人之光辉', '荒地群猎', '寒灾之咒', '险路勿近', '犹豫不决', '监工现场', '拳拳到肉', '抱头狗窜', '鸭本运作', '真相', '狂信如火', '“喜”从箱来', '竭泽而渔', '图穷匕见'])
            self.Difficulty_ch.addItems(['浪静风平', '波涛迭起', '波涛迭起·1', '波涛迭起·2', '波涛迭起·3', '波涛迭起·4', '波涛迭起·5', '波涛迭起·6',
                                        '波涛迭起·7', '波涛迭起·8', '波涛迭起·9', '波涛迭起·10', '波涛迭起·11', '波涛迭起·12', '波涛迭起·13', '波涛迭起·14', '波涛迭起·15'])
            self.Difficulty_ch.setCurrentIndex(
                config["theme_3_startdifficuilt"])
        elif theme == '探索者的银淞止境':
            self.Mission_ch.addItems(['死囚之夜', '度假村冤魂', '苔手', '待宰的兽群', '没有尽头的路', '低空机动', '违和', '幽影与鬼魅', '虫虫别回头', '弄假成真', '饥渴祭坛', '狡兽九窟', '冰海疑影', '咫尺天涯', '思维折断', '以守代攻', '大迁徙', '禁区', '坍缩体的午后', '应用测试', '公司纠葛', '杂音干扰', '求敌得敌', '本能污染',
                                     '生人勿近', '何处无山海', '乐理之灾', '亡者行军', '混乱的表象', '霜与沙', '生灵的终点', '利刃所指', '新部族', '自然之怒', '呼吸', '夺树者', '大地醒转', '巍峨银凇', '萨米之熵', '园丁', '半吊子之旅', '无中生钱', '豪华车队', '“正义使者”', '天途半道', '夙愿将偿', '惩罚', '英雄无名', '腹背受敌', '长期试用', '自然条款'])
            self.Difficulty_ch.addItems(['挑战自然', '挑战自然·1', '挑战自然·2', '挑战自然·3', '挑战自然·4', '挑战自然·5', '挑战自然·6',
                                        '挑战自然·7', '挑战自然·8', '挑战自然·9', '挑战自然·10', '挑战自然·11', '挑战自然·12', '挑战自然·13', '挑战自然·14', '挑战自然·15'])
            self.Difficulty_ch.setCurrentIndex(
                config["theme_4_startdifficuilt"])

        self.Floor_ch.setCurrentIndex(-1)
        self.Mission_ch.setCurrentIndex(-1)

        self.Confirm.setEnabled(True)
        self.Mission_ch.setEnabled(True)
        self.Difficulty_ch.setEnabled(True)
        self.Floor_ch.setEnabled(True)



    def missionChanged(self, mission):
        self.Floor_ch.clear()
        self.Mission_name.setText("你好 集批!")
        self.Blood_display.setText("")
        self.Enemy_count_display.setText("")
        self.Min_time_display.setText("")
        self.Place_display.setText("")
        self.Cost_display.setText("")
        self.Max_cost_display.setText("")
        self.Detail_display.setText("")
        self.Place_display.setText("")
        self.Cost_display.setText("")
        self.Max_cost_display.setText("")
        self.Detail_display.setText("")
        self.Enemy_list.setRowCount(0)
        self.Emergency.setChecked(False)
        file = getData(mission)
        if file != '':
            self.Floor_ch.addItems(file['Floor'])  # 层数
            if mission in ["利刃所指", "新部族", "自然之怒", "呼吸", "夺树者", "大地醒转", "巍峨银凇", "萨米之熵", "园丁""半吊子之旅", "无中生钱", "豪华车队", '“正义使者”', "天途半道", "夙愿将偿",
                           "惩罚", "英雄无名", "腹背受敌", "长期试用", "自然条款", "永恒安息", "分离与统一", "纠错", "永恒愤怒", "异体同心", "订正", "认知即重担", '“命运的宠儿”', "大群所向",
                           "人之光辉", "荒地群猎", "寒灾之咒", "险路勿近", "鸭爵与雇员", "犹豫不决", "监工现场", "拳拳到肉", "抱头狗窜", "鸭本运作", "真相", "狂信如火", '“喜”从箱来',
                           "竭泽而渔", "图穷匕见", "开门请当心", "大盗当头", "恐怖传说", "悦耳杀机", "寒渊惜别", "覆水难收", "别无所求", "诸事不顺", "再启新篇", "鸭爵表演",
                           "鸭爵的戏剧", "鸭爵的宴会", "高普尼克之拳", "这位乌萨斯人", '“骑士对决”', "邪异囚笼", "无序盛宴", "自缚", "观察"]:
                self.Emergency.setEnabled(False)
            else:
                self.Emergency.setEnabled(True)
            if len(file['Floor']) == 1:
                self.Floor_ch.setEnabled(False)
            else:
                self.Floor_ch.setEnabled(True)

    def loadEnemy(self):
        data = getData(self.Mission_ch.currentText())
        if data == '':
            self.Enemy_list.setRowCount(1)
        else:
            enemydata = data['Enemy_info']
            self.Enemy_list.setRowCount(0)
            
            for enemy_name, enemy_info in enemydata.items():
                all_hp = []
                all_atk = []
                all_def = []
                all_speed = []
                all_res = []  #da
                all_atkr = []
                all_atkd_add = []  
                all_atkd_mul = []
                #萨米 抽象
                all_hp_add = []
                all_atk_add = []
                all_def_add = []
                status_2_atk_add = []
                
                status_3_hp = []
                status_3_atk = []
                status_3_def = []
                status_2_hp = []
                status_2_atk = []
                status_2_def = []

                if self.Emergency.isChecked():
                    all_hp += data["Rune"]["hp"]
                    all_atk += data["Rune"]["atk"]
                    all_def += data["Rune"]["def"]
                    all_speed += data["Rune"]["speed"]
                    all_res += data["Rune"]["res+"]
                    all_atkr += data["Rune"]["atkr"]
                    all_atkd_add += data["Rune"]["atkd+"] 
                    all_atkd_mul += data["Rune"]["atkd*"]
                    
                if self.Theme_ch.currentText() == '傀影与猩红孤钻':
                    pass
                elif self.Theme_ch.currentText() == '水月与深蓝之树':
                    if self.Difficulty_ch.currentIndex() >= 2:
                        all_hp.append((1+(self.Difficulty_ch.currentIndex()-1)/100)**int(self.Floor_ch.currentText()))
                        all_atk.append((1+(self.Difficulty_ch.currentIndex()-1)/100)**int(self.Floor_ch.currentText()))
                    if self.Difficulty_ch.currentIndex() >= 4:
                        all_res.append(10)
                    if self.Difficulty_ch.currentIndex() >= 6:
                        status_3_atk.append(1.15)
                        status_3_def.append(1.15)
                    if self.Difficulty_ch.currentIndex() >= 8:
                        all_speed.append(1.15)
                    if self.Difficulty_ch.currentIndex() >= 10:
                        all_atkd_add.append(15)      
                    if self.Difficulty_ch.currentIndex() >= 12:
                        status_2_hp.append(1.2)
                        status_3_hp.append(1.2)
                    if self.Difficulty_ch.currentIndex() >= 13:
                        all_res.append(10)
                    if self.Difficulty_ch.currentIndex() >= 16:
                        status_2_hp.append(1.2)
                        status_2_atk.append(1.2)
                        status_2_def.append(1.2)
                        status_3_hp.append(1.2)
                        status_3_atk.append(1.2)
                        status_3_def.append(1.2)
    
                elif self.Theme_ch.currentText() == '探索者的银淞止境':
                    enemy_dict = {5:1,
                                  6:2,
                                  7:3,
                                  8:4,
                                  9:5,
                                  10:6,
                                  11:8,
                                  12:10,
                                  13:12,
                                  14:14,
                                  15:16}
                    if self.Difficulty_ch.currentIndex() >= 2:
                        all_hp.append((1+enemy_dict[self.Difficulty_ch.currentIndex()]/100)**int(self.Floor_ch.currentText()))
                        all_atk.append((1+enemy_dict[self.Difficulty_ch.currentIndex()]/100)**int(self.Floor_ch.currentText()))
                    if self.Difficulty_ch.currentIndex() >= 4:
                        status_2_atk_add.append(0.1)
                    if self.Difficulty_ch.currentIndex() >= 5:
                        all_atk_add.append(0.05)
                        all_hp_add.append(0.05)
                    if self.Difficulty_ch.currentIndex() >= 7:
                        all_def_add.append(0.15)
                    if self.Difficulty_ch.currentIndex() >= 10:
                        all_atk_add.append(0.1)      
                    if self.Difficulty_ch.currentIndex() >= 14:
                        all_def_add.append(0.05)
                        all_hp_add.append(0.05)
                    if self.Difficulty_ch.currentIndex() >= 15:
                        all_atk_add.append(0.1)
                        all_def_add.append(0.1)
                        all_hp_add.append(0.1)
                
                if enemy_info['status'] == "领袖":
                    all_hp = all_hp + status_3_hp
                    all_atk = all_atk + status_3_atk
                    all_def = all_def + status_3_def
                if enemy_info['status'] == "精英":
                    all_hp = all_hp + status_2_hp
                    all_atk = all_atk + status_2_atk
                    all_def = all_def + status_2_def
                    all_atk_add = all_atk_add + status_2_atk_add

                #region 列表显示
                self.Enemy_list.setRowCount(self.Enemy_list.rowCount() + 1)
                mName = QtWidgets.QTableWidgetItem(enemy_name)
                mName.setTextAlignment(Qt.AlignCenter)  # 设置文字显示居中
                mName.setFlags(Qt.ItemIsEnabled)  # 设置表格不可编辑模式
                self.Enemy_list.setItem(
                    self.Enemy_list.rowCount() - 1, 0, mName)

                mCount = QtWidgets.QTableWidgetItem(enemy_info['count'])
                mCount.setTextAlignment(Qt.AlignCenter)
                mCount.setFlags(Qt.ItemIsEnabled)
                self.Enemy_list.setItem(
                    self.Enemy_list.rowCount() - 1, 1, mCount)

                mStatus = QtWidgets.QTableWidgetItem(enemy_info['status'])
                mStatus.setTextAlignment(Qt.AlignCenter)
                mStatus.setFlags(Qt.ItemIsEnabled)
                self.Enemy_list.setItem(
                    self.Enemy_list.rowCount() - 1, 2, mStatus)

                mLevel = QtWidgets.QTableWidgetItem(enemy_info['level'])
                mLevel.setTextAlignment(Qt.AlignCenter)
                mLevel.setFlags(Qt.ItemIsEnabled)
                self.Enemy_list.setItem(
                    self.Enemy_list.rowCount() - 1, 3, mLevel)

                mHp = QtWidgets.QTableWidgetItem(str(round(eval(enemy_info['hp'])*FinalMultiplication(all_hp)*DirectMultiplication(all_hp_add))))
                mHp.setTextAlignment(Qt.AlignCenter)
                mHp.setFlags(Qt.ItemIsEnabled)
                self.Enemy_list.setItem(
                    self.Enemy_list.rowCount() - 1, 4, mHp)

                mAtk = QtWidgets.QTableWidgetItem(str(round(eval(enemy_info['atk'])*FinalMultiplication(all_atk)*DirectMultiplication(all_atk_add))))
                mAtk.setTextAlignment(Qt.AlignCenter)
                mAtk.setFlags(Qt.ItemIsEnabled)
                self.Enemy_list.setItem(
                    self.Enemy_list.rowCount() - 1, 5, mAtk)

                mDef = QtWidgets.QTableWidgetItem(str(round(eval(enemy_info['def'])*FinalMultiplication(all_def)*DirectMultiplication(all_def_add))))
                mDef.setTextAlignment(Qt.AlignCenter)
                mDef.setFlags(Qt.ItemIsEnabled)
                self.Enemy_list.setItem(
                    self.Enemy_list.rowCount() - 1, 6, mDef)

                mRes = QtWidgets.QTableWidgetItem(str(eval(enemy_info['res'])+DirectAddtion(all_res)))
                mRes.setTextAlignment(Qt.AlignCenter)
                mRes.setFlags(Qt.ItemIsEnabled)
                self.Enemy_list.setItem(
                    self.Enemy_list.rowCount() - 1, 7, mRes)

                mAtkd = QtWidgets.QTableWidgetItem(str((eval(enemy_info['atk_dis'])/atkd_add(all_atkd_add)*100)*FinalMultiplication(all_atkd_mul)))
                mAtkd.setTextAlignment(Qt.AlignCenter)
                mAtkd.setFlags(Qt.ItemIsEnabled)
                self.Enemy_list.setItem(
                    self.Enemy_list.rowCount() - 1, 8, mAtkd)

                mWeight = QtWidgets.QTableWidgetItem(enemy_info['weitght'])
                mWeight.setTextAlignment(Qt.AlignCenter)
                mWeight.setFlags(Qt.ItemIsEnabled)
                self.Enemy_list.setItem(
                    self.Enemy_list.rowCount() - 1, 9, mWeight)

                mSpeed = QtWidgets.QTableWidgetItem(str(eval(enemy_info['speed'])*FinalMultiplication(all_speed)))
                mSpeed.setTextAlignment(Qt.AlignCenter)
                mSpeed.setFlags(Qt.ItemIsEnabled)
                self.Enemy_list.setItem(
                    self.Enemy_list.rowCount() - 1, 10, mSpeed)
                if enemy_info['atkr'] != "—" and enemy_info['atkr'] != "全场":
                    mAtkr = QtWidgets.QTableWidgetItem(str(eval(enemy_info['atkr'])*FinalMultiplication(all_atkr)))
                else :
                    mAtkr = QtWidgets.QTableWidgetItem(enemy_info['atkr'])
                mAtkr.setTextAlignment(Qt.AlignCenter)
                mAtkr.setFlags(Qt.ItemIsEnabled)
                self.Enemy_list.setItem(
                    self.Enemy_list.rowCount() - 1, 11, mAtkr)

                mDe_blood = QtWidgets.QTableWidgetItem(enemy_info['de_blood'])
                mDe_blood.setTextAlignment(Qt.AlignCenter)
                mDe_blood.setFlags(Qt.ItemIsEnabled)
                self.Enemy_list.setItem(
                    self.Enemy_list.rowCount() - 1, 12, mDe_blood)

                #endregion
                        

            self.ene_s1.setEnabled(True)
            self.ene_s2.setEnabled(True)
            self.ene_s3.setEnabled(True)

    def ConfirmClick(self):
        if self.Mission_ch.currentText() == '':
            self.Mission_name.setText("昂?这特么哪关?")
        else:
            file = getData(self.Mission_ch.currentText())
            if file == '':
                self.Mission_name.setText("昂?这特么哪关?")
            else:
                self.Mission_name.setText(file['Mission_name'])
                self.Blood_display.setText(file['Blood'])
                self.Enemy_count_display.setText(file['Enemy_count'])
                self.Min_time_display.setText(file['Min_time'])
                if self.Emergency.isChecked():
                    self.Place_display.setText(file['Place_em'])
                    self.Cost_display.setText(file['Cost_em'])
                    self.Max_cost_display.setText(file['Max_cost_em'])
                    self.Detail_display.setText(file['Detail_em'])
                else:
                    self.Place_display.setText(file['Place'])
                    self.Cost_display.setText(file['Cost'])
                    self.Max_cost_display.setText(file['Max_cost'])
                    self.Detail_display.setText(file['Detail'])

                self.loadEnemy()
                self.setEnemylistRow(self.ene_s1)
                self.setEnemylistRow(self.ene_s2)
                self.setEnemylistRow(self.ene_s3)

    def setEnemylistCol(self, qa):
        dict = {
            'ene_name': 0,
            'ene_count': 1,
            'ene_status': 2,
            'ene_level': 3,
            'ene_hp': 4,
            'ene_atk': 5,
            'ene_def': 6,
            'ene_res': 7,
            'ene_atkd': 8,
            'ene_weight': 9,
            'ene_speed': 10,
            'ene_atkr': 11,
            'ene_deb': 12
        }
        self.Enemy_list.setColumnHidden(
            dict[qa.objectName()], not qa.isChecked())

    def setEnemylistRow(self, qa):
        dict = {
            'ene_s1': '普通',
            'ene_s2': '精英',
            'ene_s3': '领袖'
        }
        row = self.Enemy_list.rowCount()
        for i in range(row):
            if self.Enemy_list.item(i, 2).text() == dict[qa.objectName()]:
                self.Enemy_list.setRowHidden(i, not qa.isChecked())
    # endregion
