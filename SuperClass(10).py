class Shaxs:
    def __init__(self, ism, familiya, tyil, passport):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.passport = passport

    def get_info(self):
        return f"Ismi:{self.ism}, Familiyasi:{self.familiya}  yoshda:{self.get_age(2025)}  Passport:{self.passport}"
    def get_age(self, yil):
        return yil - self.tyil

class Talaba(Shaxs):
    def __init__(self,ism,familiya,tyil,passport,manzil):
        super().__init__(ism,familiya,tyil,passport)
        self.manzil = manzil
        self.fanlar=[]

    def fan_qoshish(self,fan):
        self.fanlar.append(fan)

    def fanlar_p(self):
        if self.fanlar:
            fanlar_str = ", ".join([fan.nomi for fan in self.fanlar])
            return f"Siz {fanlar_str} fanlariga yozilgansiz."
        else:
            return "Siz hali birorta fanga yozilmadingiz."

    def remove_fan(self):
        if self.fanlar:
            self.fanlar.remove(self.fanlar[0])
            #       {self.fanlar[0]}
            print(f"fan ochirildi",)
        else:
            print("bunday fanga yozilmagan siz")



class Manzil:
    def __init__(self,viloyat,shaxxar,mahalla,uy):
        self.viloyat = viloyat
        self.shaxxar = shaxxar
        self.mahalla = mahalla
        self.uy = uy

    def get_manzil(self):
        manzil= f"{self.viloyat} viloyati, {self.shaxxar} shahri, {self.mahalla} mahallasi, {self.uy}-uy"
        return manzil

class Fan:
    def __init__(self,nomi):
        self.nomi = nomi


class Foydalanuvchi(Shaxs):
    def __init__(self,ism,familiya,tyil,passport,vakolati):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.passport = passport
        self.vakolati = vakolati

    def get_info(self):
        return f"Ismi:{self.ism} Familiyasi:{self.familiya} Yoshda:{self.get_age(2025)}  Passport:{self.passport} Vakolati: {self.vakolati}"


class Admin(Foydalanuvchi):
    def __init__(self,ism,familiya,tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil

    def ban_info(self):
        return f"{self.ism} {self.familiya}, {self.tyil}: Foydalanuvchi bloklandi !"



talaba_m = Manzil("Xorazim","urgench","najmudun, kubro","70,11")
talaba1 = Talaba("Javohir","Ismoilov",2006,"AD5861793",talaba_m)

matematika = Fan("Matematika")
fizika = Fan("Fizika")
informatika = Fan("Informatika")

talaba1.fan_qoshish(matematika)
talaba1.fan_qoshish(fizika)
talaba1.fan_qoshish(informatika)


hodim= Foydalanuvchi("Temur","Amirov",1996,"CA4795138","Prafessir")

user_ban = Admin("Joxa","Palonchiyiv",2010)

print(talaba1.get_info())
print("Manzili:", talaba1.manzil.get_manzil())
print(talaba1.fanlar_p())
print(talaba1.remove_fan())
print(talaba1.fanlar_p())

print(hodim.get_info())

print(user_ban.ban_info())