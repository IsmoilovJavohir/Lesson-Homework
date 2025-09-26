# class User:
#     def __init__(self, name,age,email, password,):
#         self.ism = name
#         self.yosh = age
#         self.email = email
#         self.password = password
#     def user_info(self):
#         return f"\nIsm:{self.ism}\n Yoshi:{self.yosh}\n  pochta manzili:{self.email}     email paroli:{self.password}"
#
# foydalanuvchi = User(input("Foydalanuvchi ismni kirzing: "),input("Foydalanuvchi yoshini kirizing: "),input("Pochta manzilingizni kirizing: "),input("email manzilini parolini kirizing: "))
# print(foydalanuvchi.user_info())
from os import remove


##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# class Avto:
#     def __init__(self, model, karobka, rang, yil, km, narx):
#         self.model = model
#         self.karobka = karobka
#         self.rang = rang
#         self.km = km
#         self.narx = narx
#         self.yil = yil
#
#     # def get_km(self, new_km):
#     #     a=self.km = new_km
#     #     return self.km + new_km
#
#
#     def avto_info(self):
#         return f"Mashina: {self.model}  Korobka: {self.karobka}   rangi: {self.rang}  Yili:{self.yil}   Km:{self.km}  Narx:{self.narx} so\'m"
#
# avtomobillar= Avto("Ekonix", "Avtomat", "qora", 2023, 20000, 400000000)
# print(avtomobillar.avto_info())
# # km_input = int((input("km: ")))
# # Avto.get_km(a)

##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class Avto_salon:
    def __init__(self,ismi, manzzil, telifonraqami, avtamabilar):
        self.ismi1 = ismi
        self.manzzil1 = manzzil
        self.telifonraqami1 = telifonraqami
        self.avtamabilar1 = avtamabilar

    def get_info(self):
        return (f"{self.ismi1} "
                f"manzili:{self.manzzil1} "
                f"telifonraqami:{self.telifonraqami1} "
                f"sotuvdagi avtamabilar:{self.avtamabilar1}")

avto1= Avto_salon("Uz motors", "Xanqa", +998000000000,"Damas, Labo, Spark, Tracker")
avto2= Avto_salon("Super motors", "xiva", +998888970550,"Equinox, Traverse, Spark, Tracker")
print(avto1.get_info())
print(avto2.get_info())
a=dir()
for joxa in a:
    if joxa.startswith("__")==False:
        print(joxa)
