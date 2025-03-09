
from abc import ABC, abstractmethod

class ATM(ABC):
    def __init__(self):
        self.balance = 0
        self.pin =''


class Menu(ATM):
    def __init__(self,tanlovlari):
        super().__init__("menu")
        self.tanlovlari = tanlovlari
        user_input = int(input("""
        1 pin o'rnatish
        2 balanse to'ldirish
        3 balansni tekshirish
        4 pul yechish
        5 pin kodni o'zgartirish
        0 chiqish uchun
        """))
        if user_input == 1:
            "pin o'rnatish"
            self.tanlovlari.set_pin()
        # elif user_input == 2:
        #     "balanse to'ldirish "
        #     self.fill_balance()
        # elif user_input == 3:
        #     "balansni tekshirish "
        #     self.check_balnce()
        # elif user_input == 4:
        #     "pul yechish "
        #     self.withard()
        # elif user_input == 5:
        #     "pin kodni o'zgartirish "
        #     self.change_pin()
        # elif user_input == 0:
        #     exit()
        # else:
        #     print("Buzdingiz !!!")
