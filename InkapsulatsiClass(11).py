class Shaxs:
    odamlar_soni = 0
    def __init__(self,ism, familiya, idcard, tyil,):
        self.__ism = ism
        self.familiya = familiya
        self.__idcard = idcard
        self.tyil = tyil

        Shaxs.odamlar_soni += 1

    def get_ism(self):
        return self.__ism
    def get_idcart(self):
        return self.__idcard
    def get_info(self):
        return f"Ism:{Shaxs.get_ism(self)} Familiyasi:{self.familiya}. {Shaxs.get_idcart(self)}:Passport raqami  {self.tyil}:Tug'ulgan"

    @classmethod
    def insonlar_soni(cls):
        return f"Jamiy insonlar soni: {cls.odamlar_soni}"


class Talaba(Shaxs):
    t_soni = 0
    def __init__(self,ism,familiya, idcard, tyil, bosqich):
        super().__init__(ism,familiya,idcard,tyil)
        self.bosqich = bosqich

        Talaba.t_soni += 1

    def get_age(self,yil):
        return yil - self.tyil

    def get_ism(self):
            return self.__ism

    def get_idcart(self):
            return self.__idcard

    def get_bosqich(self):
        return self.bosqich

    def get_info1(self):
        return f"Ism:{Shaxs.get_ism(self)} Familiyasi:{self.familiya}. {Shaxs.get_idcart(self)}:Passport raqami  {self.get_age(2025)}:Yoshda {self.bosqich}-Bosqich talabasi"


    @classmethod
    def talabalar_soni(cls):
        return f"Jamiy talabalar mavjud: {cls.t_soni}"

    @classmethod
    # 3-savol uchun
    def new_s(cls, yangi_s):
        cls.t_soni = yangi_s

Talaba.new_s(10)

inson1= Shaxs("Javohir","Ismoilov","BS5879614",2001)
inson2= Shaxs("Lobar","Boltavayiva","HT584899",1999)

print(inson1.get_info())#,inson2.get_info())
print(inson2.get_info())

inson2=Talaba("Joxa","palonchiyiv","AD844658",1998,3)
inson3=Talaba("Jamol","palonchiyiv","DS997566",2000,2)
inson4=Talaba("Shoxrux","palonchiyiv","ER884515",2004,1)


print(inson2.get_info1())
print(inson3.get_info1())
print(inson4.get_info1())

print(Shaxs.insonlar_soni())
print(Talaba.talabalar_soni())

