from logging import critical

from PyQt5.QtWidgets import QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QTextEdit, QDialog, QHBoxLayout, QLabel, \
    QComboBox, QWidget


class STR(QWidget):
    def __init__(self, attack_style):
        super().__init__()

        self.attack_style = attack_style
        # 连击
        self.hit_count_box = None
        self.hit_count_type_box = None
        self.skill_level_combox = None
        self.main_layout = None
        self.resize(800, 800)

        # 加攻
        self.normal_ATK_up_lowest_box = None
        self.normal_ATK_up_highest_box = None
        self.normal_ATK_up_count_box = None
        self.normal_ATK_up_INT_box = None

        self.element_ATK_up_lowest_box = None
        self.element_ATK_up_highest_box = None
        self.element_ATK_up_count_box = None
        self.element_ATK_up_INT_box = None

        # 减防
        self.normal_defend_off_highest_box = None
        self.normal_defend_off_lowest_box = None
        self.normal_defend_off_count_box = None
        self.normal_defend_off_INT_box = None
        self.normal_defend_off_LCK_box = None

        self.element_defend_off_lowest_box = None
        self.element_defend_off_highest_box = None
        self.element_defend_off_count_box = None
        self.element_defend_off_INT_box = None
        self.element_defend_off_LCK_box = None

        # 暴击
        self.critical_rate_box = None
        self.critical_damage_box = None

        # 场地
        self.field_box = None

        # 心眼
        self.mindEye_box = None
        self.mindEye_count_box = None

        # 脆弱
        self.weakness_highest_box = None
        self.weakness_lowest_box = None
        self.weakness_count_box = None
        self.weakness_INT_box = None
        self.weakness_LCK_box = None

        # 定义功能
        self.calculate_btn = None
        self.save_btn = None

        # 定义数据（文本框）
        self.STR_box = None  # 力量
        self.DEX_box = None  # 灵巧
        self.VIT_box = None  # 体力
        self.SPR_box = None  # 精神
        self.INT_box = None  # 智慧
        self.LCK_box = None  # 运气
        self.skill_highest_box = None
        self.skill_lowest_box = None
        self.enemy_border_box = None
        self.effect_par_cap_box = None

        # 定义有关变量
        self.enemy_border = None

        # 输出结果标签
        self.result_label = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Heaven Burns Red")
        self.setGeometry(1000, 500, 800, 800)

        # 布局
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # 角色六维数据
        if self.attack_style == "2*STR+1*DEX" or self.attack_style == "1*STR+2*DEX" or self.attack_style == "1*STR+1*DEX":
            self.STR_box = self.my_input("力量:")
            self.DEX_box = self.my_input("灵巧:")
        elif self.attack_style == "1*VIT":
            self.VIT_box = self.my_input("体力:")
        elif self.attack_style == "1*INT":
            self.INT_box = self.my_input("智慧:")
        else:
            self.SPR_box = self.my_input("精神:")
            self.LCK_box = self.my_input("运气:")

        # 技能数据
        self.skill_lowest_box = self.my_input("技能伤害下限(1级):")
        self.skill_highest_box = self.my_input("技能伤害上限(1级):")
        self.effect_par_cap_box = self.my_input("技能属性差值:")
        self.skill_level_combox = self.my_combox("技能等级:", "skill_level")

        # 敌人属性
        self.enemy_border_box = self.my_input("敌人属性:")

        # 连击珠
        self.hit_count_type_box, self.hit_count_box = self.my_combox("连击珠类型:", "hit")
        # self.hit_count_box = self.my_combox("连击珠层数:","hit_count")
        self.hit_INT_box = self.my_input("提供连击增益的角色智慧值:")

        # 加攻
        self.normal_ATK_up_lowest_box = self.my_input("普通加攻下限:")
        self.normal_ATK_up_highest_box = self.my_input("普通加攻上限:")
        self.normal_ATK_up_count_box = self.my_combox("普通加攻层数:", "count")
        # self.normal_ATK_up_INT_box = self.my_input("提供普通加攻增益的角色智慧值:")

        self.element_ATK_up_lowest_box = self.my_input("元素加攻下限:")
        self.element_ATK_up_highest_box = self.my_input("元素加攻上限:")
        self.normal_ATK_up_count_box = self.my_combox("元素加攻层数:", "count")
        # self.element_ATK_up_INT_box = self.my_input("提供元素加攻增益的角色智慧值:")

        # 减防
        self.normal_defend_off_lowest_box = self.my_input("普通减防下限:")
        self.normal_defend_off_highest_box = self.my_input("普通减防上限:")
        self.normal_defend_off_count_box = self.my_combox("普通减防层数:", "count")
        self.normal_defend_off_INT_box = self.my_input("提供普通减防的角色智慧值:")
        self.normal_defend_off_LCK_box = self.my_input("提供普通减防的角色运气值:")

        self.element_defend_off_lowest_box = self.my_input("元素减防下限:")
        self.element_defend_off_highest_box = self.my_input("元素减防上限:")
        self.normal_defend_off_count_box = self.my_combox("元素减防层数:", "count")
        self.element_defend_off_INT_box = self.my_input("提供普通减防的角色智慧值:")
        self.element_defend_off_LCK_box = self.my_input("提供普通减防的角色运气值:")

        # 暴击
        self.critical_rate_box = self.my_input("暴击率:")
        self.critical_damage_box = self.my_input("暴击伤害:")

        # 心眼
        self.mindEye_box = self.my_input("心眼:")
        self.mindEye_count_box = self.my_combox("心眼层数:", "count")

        # 脆弱
        self.weakness_highest_box = self.my_input("脆弱上限:")
        self.weakness_lowest_box = self.my_input("脆弱下限:")
        self.weakness_count_box = self.my_input("脆弱层数")
        self.weakness_INT_box = self.my_input("请输入提供脆弱的角色智慧值:")
        self.weakness_LCK_box = self.my_input("请输入提供脆弱的角色运气值:")

        # 场地
        self.field_box = self.my_combox("场地:", "field")

        # 结果显示区
        self.result_label = QTextEdit("结果将显示在这里", self)
        self.main_layout.addWidget(self.result_label)

        # 数据保存
        self.save_btn = QPushButton("保存输入数据")
        self.save_btn.clicked.connect(self.on_save)
        self.main_layout.addWidget(self.save_btn)

        # 数据计算
        self.calculate_btn = QPushButton("计算")
        self.calculate_btn.clicked.connect(self.basic_damage)
        self.main_layout.addWidget(self.calculate_btn)

        # 获取敌人属性值
    def enemy(self):
        try:
            self.enemy_border = self.enemy_border_box.text()
            self.enemy_border = int(self.enemy_border)
        except:
            QMessageBox.information(self, 'Notice', "请稍后输入敌人属性！", QMessageBox.Yes)

    def calculate(self, max_data, min_data, par_cap, character_data, _type):
        self.enemy()
        cap = character_data - self.enemy_border
        if _type == "damage":
            if cap > par_cap:
                return max_data
            elif 0 < cap <= par_cap:
                return (max_data - min_data) / par_cap * cap + min_data
            elif (-par_cap / 2) < cap <= 0:
                return (min_data - 1) / (par_cap / 2) * cap + min_data
            else:
                return 1
        else:
            if cap > par_cap:
                return max_data
            elif 0 < cap <= par_cap:
                return (max_data - min_data) / par_cap * cap + min_data
            else:
                return min_data

    def basic_damage(self):

        # 角色数据
        if self.attack_style == "2*STR+1*DEX" or self.attack_style == "1*STR+2*DEX" or self.attack_style == "1*STR+1*DEX":
            STR = self.STR_box.text()
            DEX = self.DEX_box.text()
        elif self.attack_style == "1*VIT":
            VIT = self.VIT_box.text()
        elif self.attack_style == "1*INT":
            INT = self.INT_box.text()
        else:
            pass

        # 暴击
        critical_rate = self.critical_rate_box.text()
        critical_damage = self.critical_damage_box.text()

        # 技能数据
        skill_lowest = self.skill_lowest_box.text()
        skill_highest = self.skill_highest_box.text()
        effect_par_cap = self.effect_par_cap_box.text()

        try:

            if self.attack_style == "2*STR+1*DEX":
                STR = int(STR)
                DEX = int(DEX)
                character_data = 2 * STR + 1 * DEX
            elif self.attack_style == "1*STR+2*DEX":
                STR = int(STR)
                DEX = int(DEX)
                character_data = 1 * STR + 2 * DEX
            elif self.attack_style == "1*STR+1*DEX":
                STR = int(STR)
                DEX = int(DEX)
                character_data = 1 * STR + 1 * DEX
            elif self.attack_style == "1*VIT":
                VIT = int(VIT)
                character_data = VIT

            elif self.attack_style == "1*INT":
                INT = int(INT)
                character_data = INT
            else:
                character_data = 0
            skill_lowest = int(skill_lowest)
            skill_highest = int(skill_highest)
            effect_par_cap = int(effect_par_cap)
            critical_damage = float(critical_damage)
            critical_rate = float(critical_rate)
            print(self.enemy_border)
            critical_basic_damage = (critical_damage+1)* self.calculate(skill_highest, skill_lowest, effect_par_cap,
                                                                     50 + character_data, "damage")
            incritical_basic_damage = self.calculate(skill_highest, skill_lowest, effect_par_cap, character_data,
                                                     "damage")
            if critical_rate > 1:
                basic_damage = critical_basic_damage
            elif 0 < critical_rate <= 1:
                basic_damage = critical_basic_damage * critical_rate + incritical_basic_damage * (1 - critical_rate)
            else:
                basic_damage = incritical_basic_damage = 0


            self.result_label.setText(
                f"不暴击基础伤害为{incritical_basic_damage},暴击基础伤害为{critical_basic_damage},期望为{basic_damage}")
            return basic_damage
        except:
             QMessageBox.information(self, 'Notice', "基础输入有误，请重新输入！", QMessageBox.Yes)

    def attack_up(self):
        normal_attack_up = self.normal_ATK_up_highest_box.text()
        normal_attack_up_count = self.normal_ATK_up_count_box.currentText()
        element_attack_up = self.element_ATK_up_highest_box.text()
        element_attack_up_count = self.element_ATK_up_count_box.currentText()
        try:
            normal_attack_up = float(normal_attack_up)
            element_attack_up = float(element_attack_up)
            normal_attack_up_count = int(normal_attack_up_count)
            element_attack_up_count = int(element_attack_up_count)
            return normal_attack_up * normal_attack_up_count + element_attack_up * element_attack_up_count
        except:
            QMessageBox.information(self, 'Notice', "加工输入有误，请重新输入！", QMessageBox.Yes)

    def defend_off(self):
        normal_defend_off_lowest = self.normal_defend_off_lowest_box.text()
        normal_defend_off_highest = self.normal_defend_off_highest_box.text()
        normal_defend_off_count = self.normal_defend_off_count_box.currentText()
        normal_defend_off_INT = self.normal_defend_off_INT_box.text()
        normal_defend_off_LCK = self.normal_defend_off_LCK_box.text()

        element_defend_off_lowest = self.element_defend_off_lowest_box.text()
        element_defend_off_highest = self.element_defend_off_highest_box.text()
        element_defend_off_count = self.element_defend_off_count_box.currentText()
        element_defend_off_INT = self.element_defend_off_INT_box.text()
        element_defend_off_LCK = self.element_defend_off_LCK_box.text()

        try:
            normal_defend_off_lowest = float(normal_defend_off_lowest)
            normal_defend_off_highest = float(normal_defend_off_highest)
            normal_defend_off_count = int(normal_defend_off_count)
            normal_defend_off_INT = int(normal_defend_off_INT)
            normal_defend_off_LCK = int(normal_defend_off_LCK)

            element_defend_off_lowest = float(element_defend_off_lowest)
            element_defend_off_highest = float(element_defend_off_highest)
            element_defend_off_count = int(element_defend_off_count)
            element_defend_off_INT = int(element_defend_off_INT)
            element_defend_off_LCK = int(element_defend_off_LCK)

            normal_cap = 2 * normal_defend_off_INT + normal_defend_off_LCK
            element_cap = 2 * element_defend_off_INT + element_defend_off_LCK

            return normal_defend_off_count * self.calculate(normal_defend_off_highest, normal_defend_off_lowest, 123,
                                                            normal_cap,
                                                            "debuff") + element_defend_off_count * self.calculate(
                element_defend_off_highest, element_defend_off_lowest, 123, element_cap, "debuff")
        except:
            QMessageBox.information(self, 'Notice', "减防输入有误，请重新输入！", QMessageBox.Yes)

    def hit(self):
        hit_type = self.hit_count_type_box.currentText()
        hit_count = self.hit_count_box.currentText()
        if hit_type == "特大(80%)":
            hit_damage = 0.8
        elif hit_type == "大(40%)":
            hit_damage = 0.4
        elif hit_type == "小(50%)":
            hit_damage = 0.5
        else:
            hit_damage = 0

        try:
            hit_count = int(hit_count)
            return hit_count * hit_damage
        except:
            QMessageBox.information(self, 'Notice', "连击输入有误，请重新输入！", QMessageBox.Yes)

    def mind_eye(self):
        mindEye = self.mindEye_box.text()
        mindEye_count = self.mindEye_count_box.currentText()
        try:
            mindEye = float(mindEye)
            mindEye_count = float(mindEye_count)
            return mindEye * mindEye_count
        except:
            QMessageBox.information(self, 'Notice', "心眼输入有误，请重新输入！", QMessageBox.Yes)

    def weak(self):
        weakness_highest = self.weakness_highest_box.text()
        weakness_lowest = self.weakness_lowest_box.text()
        weakness_count = self.weakness_count_box.currentText()
        weakness_INT = self.weakness_INT_box.text()
        weakness_LCK = self.weakness_LCK_box.text()
        try:
            weakness_highest = float(weakness_highest)
            weakness_lowest = float(weakness_lowest)
            weakness_count = int(weakness_count)
            weakness_INT = int(weakness_INT)
            weakness_LCK = int(weakness_LCK)
            return self.calculate(weakness_highest, weakness_lowest, 141, 2 * weakness_LCK + weakness_INT, "weak")
        except:
            QMessageBox.information(self, 'Notice', "脆弱输入有误，请重新输入！", QMessageBox.Yes)

    def field(self):
        _field = self.field_box.currentText()
        try:
            _field = float(_field)
            return _field
        except:
            QMessageBox.information(self, 'Notice', "场地输入有误，请重新输入！", QMessageBox.Yes)

    # def final_damage(self):
    #     fdamage = self.basic_damage()*self.attack_up()*self.defend_off()*self.hit()*self.mind_eye()*self.weak()*self.field()

    def my_input(self, label_text):
        layout = QHBoxLayout()
        layout.addWidget(QLabel(label_text))
        input_box = QLineEdit()
        layout.addWidget(input_box)
        self.main_layout.addLayout(layout)
        return input_box

    def my_combox(self, label_text, combo_type):
        layout = QHBoxLayout()
        layout.addWidget(QLabel(label_text))

        # 等级选择框
        if combo_type == "skill_level":
            skill_level = QComboBox()
            skill_level.addItems(["1", "2", "3", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"])
            layout.addWidget(skill_level)
            self.main_layout.addLayout(layout)
            return skill_level


        # 连击
        elif combo_type == "hit":
            # 连击类型选择框
            hit_count_type = QComboBox()
            hit_count_type.addItems(["特大(80%)", "大(40%)", "小(50%)"])
            layout.addWidget(hit_count_type)

            # 连击珠层数选择框
            layout.addWidget(QLabel("连击珠层数:"))
            hit_count = QComboBox()
            hit_count.addItems(["0", "3", "5", "6", "10"])
            layout.addWidget(hit_count)

            self.main_layout.addLayout(layout)
            return hit_count_type, hit_count

        # 场地选择框
        elif combo_type == "field":
            field = QComboBox()
            field.addItems({"0.5", "0.65", "0.8"})
            layout.addWidget(field)
            self.main_layout.addLayout(layout)
            return field

        # buff/debuff层数选择框
        elif combo_type == "count":
            count = QComboBox()
            count.addItems({"1", "2"})
            layout.addWidget(count)
            self.main_layout.addLayout(layout)

        else:
            pass

    def on_save(self):
        QMessageBox.information(self, 'Notice', "功能开发中，敬请期待...")
    # reply = QMessageBox.information(self, 'Notice', "Are you sure to want to save?",
    #                                 QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    # if reply == QMessageBox.Yes:
    #     QMessageBox.information(self, 'Notice', "The data has been saved successfully!")
    #     self.close()
    # else:
    #     QMessageBox.information(self, 'Notice', "save failed")

# def back(self):
#     reply = QMessageBox.information(self,'Notice','确认？',QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes)
#     if reply == QMessageBox.Yes:
#         menu = Style()
#         menu.show()
#         self.close()
#     else:
#         pass
