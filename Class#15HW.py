class User:
    def __init__(self, name,age,email, password,):
        self.ism = name
        self.yosh = age
        self.email = email
        self.password = password
    def user_info(self):
        return f"\nIsm:{self.ism}\n Yoshi:{self.yosh}\n  pochta manzili:{self.email}     email paroli:{self.password}"

foydalanuvchi = User(input("Foydalanuvchi ismni kirzing: "),input("Foydalanuvchi yoshini kirizing: "),input("Pochta manzilingizni kirizing: "),input("email manzilini parolini kirizing: "))
print(foydalanuvchi.user_info())

##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

class Avto:
    def __init__(self, model, karobka, rang, yil, km, narx):
        self.model = model
        self.karobka = karobka
        self.rang = rang
        self.km = km
        self.narx = narx
        self.yil = yil

    def avto_info(self):
        return f"Mashina: {self.model}  Korobka: {self.karobka}   rangi: {self.rang}  Yili:{self.yil}   Km:{self.km}  Narx:{self.narx} so\'m"

avtomobillar= Avto("Ekonix", "Avtomat", "qora", 2023, 20000, 400000000)
print(avtomobillar.avto_info())

##\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# class Avto_salon:
#     def __init__(self,name, manzzil, avtamabilar):
#         self.name = name