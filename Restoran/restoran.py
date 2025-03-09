print("Assalomu aleykum siz nu yerda kartangizdagi ma'lumotlarni ko'rib Taomlarga buyurtma berishingiz mumkin.")
class SOFFATM:
    def __init__(self):
        self.pin = ""
        self.balnace = 0
        self.restoranga = Restoran(self)



    def menu(self):
        while True:
            user_input = input(
            """
        💳Siz Bu yerda kartangizni boshqarishiz mumkin.
    1 🔢pin o'rnatish
    2 🔄balanse to'ldirish 
    3 💰balansni tekshirish 
    4 🔄pul yechish 
    5 🔢 pin kodni o'zgartirish 
    6 🏪restoranga o'tish
    0 🔄chiqish uchun
            """
            )
            if user_input == "1":
                "🔢pin o'rnatish"
                self.set_pin()
            elif user_input == "2":
                "💰balanse to'ldirish "
                self.fill_balance()
            elif user_input == "3":
                "💵balansni tekshirish "
                self.check_balnce()
            elif user_input == "4":
                "💳pul yechish "
                self.withard()
            elif user_input == "5":
                "🔢pin kodni o'zgartirish "
                self.change_pin()
            elif user_input == "6":
                self.restoranga.menu1()
            elif user_input == "0":
                self.menu()
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




class Restoran:

    def __init__(self,atm):
        self.atm = atm


    def menu1(self):
        while True:
            dick = input(
        """
    🏪 Restoran
    1 🍹ichimliklar
    2🍝 taomlar
    3🛒 buyurma berish
        """
        )
            if dick == "1":
                print("🍹Ichimliklar ro'yxatini ")
                self.ichimliklar()
            elif dick == "2":
                print("🍝Taomlar ro'yxati")
                self.taomlar()
            elif dick == "3":
                print("🛒Siz bu yerda buyurtma berishingiz mumkin")
                self.buyurtma_berish()
            elif dick == "4":
                pass
            elif dick == "5":
                pass
            else:
                print("Iltimos menudagi raqamlarga qarab tanlang")


    def ichimliklar(self):

        exit = input("""
    1.Olma sharbati =10 ming
    2.O'rik sharbati =2 ming
    3.sharbat =4 ming
    4.Cola = 10 ming
    5.Fanta = 11ming
    6.Milliy cola =10 ming
    7.Ko'k choy = 2 ming
    8.limon choy = 5 ming
    9.qora choy = 3 ming
    10. mevali choy = 8 ming
     BU bo'limdan chiqishingiz uchun 0 ni kiriting
        """)
        if exit == "0":
            self.menu1()
        else:
            print("Bu yerda siz 0 ni kiriting ")


    def taomlar(self):
        exit = input("""
        1. Sho'rva = 4 ming
        2. Osh = 7ming
        3. Shashlik 1-sixi = 1000 so'm
        4. somsa = 500 so'm
        5. prashka = 100 so'm
        6. qozon kabaob = 2ming
        7. lavash = 1000so'm
        Menu ga qaytish uchun 0 ni bosing
        """)
        if exit == "0":
            self.menu1()
        else:
            "Kechirasiz menuga qaytish uchun 0 ni bosing"

    def buyurtma_berish(self):
        ichimliklar = {
            1: ("Olma sharbati", 10),
            2: ("O'rik sharbati", 2),
            3: ("Sharbat", 4),
            4: ("Cola", 10),
            5: ("Fanta", 110),
            6: ("Milliy cola", 10),
            7: ("Ko'k choy", 2),
            8: ("Limon choy", 5),
            9: ("Qora choy", 3),
            10: ("Mevali choy", 8),
        }

        taom = {
            1:("Sho'rva",4),
            2:("osh",7),
            3:("shashlik 1sixi",1),
            4:("Somsa",0.5),
            5:("prashka",0.1),
            6:("Qozon kabob",2),
            7:("Lavash",1)
        }
        jami_buyurtmalar = []
        jami_summa = 0
        # Ro‘yxatni chiqarish
        while True:
            ichimlik_menyu = "\n".join([f"{key}. {nomi} = {narx} so'm" for key, (nomi, narx) in ichimliklar.items()])

            tanlov = int(
                input(f"\n{ichimlik_menyu}\n\n 🛒 Qaysi ichimlikni tanlaysiz? (Menyuga qaytish uchun 0 ni kiriting ??? Aks xolda -1 ni bosib keyinig bo'limga o'ting): "))

            if tanlov == 0:
                 self.menu1()
            elif tanlov in ichimliklar:
                nomi, narx = ichimliklar[tanlov]
                jami_buyurtmalar.append(nomi)
                jami_summa += narx
                print(f"✅{nomi} tanlandi. Narxi: {narx} so'm")
            elif tanlov == -1:
                break
            else:
                print("❌Noto‘g‘ri tanlov!")
                ichimlik_menyu

        while True:
            taomlar_menyu = "\n".join([f"{key}. {nomi} = {narx} so'm" for key, (nomi, narx) in taom.items()])
            tanlov = int(input(
                f"\n{taomlar_menyu}\n\n🍝Qaysi taomni tanlaysiz?\n"
                "🡆 Menyuga qaytish uchun 0\n"
                "🡆 Buyurtmani yakunlash uchun -1 kiriting: "
            ))

            if tanlov == 0:
                return self.menu1()
            elif tanlov == -1:
                break  # **Buyurtmani yakunlash**
            elif tanlov in taom:
                nomi, narx = taom[tanlov]
                jami_summa += narx
                jami_buyurtmalar.append(nomi)
                print(f"✅ {nomi} tanlandi. Narxi: {narx} so'm")
            else:
                print("⚠ Noto‘g‘ri tanlov! Iltimos, qaytadan kiriting.")
                taomlar_menyu

        print("\n 🛒Sizning buyurtmangiz")
        for i, buyurtma in enumerate(jami_buyurtmalar,1):
            print(f"{i}.{buyurtma}")
        print(f"\n🛒 Jami summa: {jami_summa} so'm")
        print("agar buyutmani rasmiylashtirmoqchi bo'lsangiz tolov qiling")
        oxirgi = input(f"siz hisobingizdan {jami_summa}ming yechilmoqda??(Hechilishini hoxlasangiz ha/yo'qni bosing")
        if oxirgi.lower() =="ha":
            if self.atm.balnace >= jami_summa:
                self.atm.balnace -= jami_summa
                print("✅ Buyurtmangiz qabul qilindi! Rahmat! 😊\n")
                print(f"💰Sizda hozir kartangizda {self.atm.balnace} qoldi")
                exit()
            else:
                print("❌Sizning hisobingizda yetarli mablag' yo'q")
                print("🏧Agar siz buyurtma qilish uchun balance to'ldiring(uning uchun siz kaztazga pul tashlang)")
                self.atm.menu()
        elif oxirgi.lower() == "yo'q":
            print("❌Buyurtma bekor qilindi")
            print("🔄Qaytadan buyurtma bermoqchimisiz")
            qaytadan = input("Qaytadan buyurtma bermoqchimisiz? (ha/yo'q)")
            if qaytadan.lower() == "ha":
                self.menu1()
            elif qaytadan.lower() == "yo'q":
                exit()
        else:
            print("Siz ha yoki yo'q ni kiriting")

atm = SOFFATM()
atm.menu()
res = Restoran()
res.menu1()
