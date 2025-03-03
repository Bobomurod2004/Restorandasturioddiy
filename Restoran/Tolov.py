
class SOFFATM:
    def __init__(self):
        self.pin = ""
        self.balnace = 0
        self.menu()

    def menu(self):
        user_input = int(input(
            """
    1 pin o'rnatish
    2 balanse to'ldirish 
    3 balansni tekshirish 
    4 pul yechish 
    5 pin kodni o'zgartirish 
    0 chiqish uchun
            """
        ))
        if user_input == 1:
            "pin o'rnatish"
            self.set_pin()
        elif user_input == 2:
            "balanse to'ldirish "
            self.fill_balance()
        elif user_input == 3:
            "balansni tekshirish "
            self.check_balnce()
        elif user_input == 4:
            "pul yechish "
            self.withard()
        elif user_input == 5:
            "pin kodni o'zgartirish "
            self.change_pin()
        elif user_input == 0:
            exit()
        else:
            print("Buzdingiz !!!")

    def set_pin(self):
        pin = input("pin kiriting. ")
        if len(pin) == 4:
            self.pin = pin
            print(f"pin o'rnatildi >> {pin}")
        else:
            print("Faqat 4 xonali bo'lsin")
        self.menu()

    def fill_balance(self):
        try:
            balance = int(input("summa kiriting: "))
            self.balnace = balance
            print(f"sizning balansingiz: {balance}")
        except:
            print("faqat son kiriting")
        finally:
            self.menu()

    def check_balnce(self):
        pin = input("pin kiriting: ")
        if self.pin == pin:
            print(f"sizing hisobingiz : {self.balnace}")
        else:
            print("sizning pin kodingiz xato")
        self.menu()

    def withard(self):
        pin = input("pin kiritng: ")
        amount = int(input("nechapul yechmoqchisiz: "))
        old_balance = self.balnace
        if self.balnace >= amount:
            self.balnace = self.balnace - amount
            print(f"sizda {old_balance} bor edi , endi {self.balnace} qoldi")
        else:
            print("hisobingizda yetarli mablag' yo'q ")
        self.menu()

    def change_pin(self, new_pin=None):
        old_pin = self.pin
        input_old_pin = input("eski parolingizni kiriting: ")
        if old_pin == input_old_pin:
            if len(new_pin) == 4:
                new_pin = input("yangi pin kiriting: ")
                old_pin = new_pin
                print(f"parolingiz {new_pin} ga o'zgardi")
            else:
                print("4 xonali kiriting:")
        else:
            print("Bankga boring")
        self.menu()


atm = SOFFATM()
