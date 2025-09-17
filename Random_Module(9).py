#                                          №1

# Usul seed()tasodifiy sonlar generatorini ishga tushirish uchun ishlatiladi.
import random
random.seed(10)
print(random.random())

import random
random.seed(100)
print(random.random())

print("/////////////////////////////////////////////////// 2")
#                                          №2

# Usul getstate()tasodifiy sonlar generatorining joriy holatiga ega ob'ektni qaytaradi.
import random
x= random.getstate()
print(x)

import random
a= random.setstate(x)
print(a)

print("/////////////////////////////////////////////////// 3")
#                                          №3

# Usul setstate()tasodifiy sonlar generatorining holatini belgilangan holatga qaytarish uchun ishlatiladi
import random
print(random.random())

ozgaruvchi = random.getstate()
print(random.random())

random.setstate(ozgaruvchi)
print(random.random())


print("/////////////////////////////////////////////////// 4")
#                                          №4

# Usul getrandbits()belgilangan o'lchamdagi (bitlarda) butun sonni qaytaradi.
import random
print(random.getrandbits(11))
print(random.getrandbits(8))


print("/////////////////////////////////////////////////// 5")
#                                          №5

# Usul randrange()belgilangan diapazondan tasodifiy tanlangan elementni qaytaradi.
import random
print(random.randrange(3,100))
print(random.randrange(22,100, 5))


print("/////////////////////////////////////////////////// 6")
#                                          №6

# Usul randint()belgilangan diapazondan tanlangan elementning butun sonini qaytaradi.
import random
print(random.randint(3,9))
print(random.randint(3,9+1))


print("/////////////////////////////////////////////////// 7")
#                                          №7

# Usul choice()belgilangan ketma-ketlikdan tasodifiy tanlangan elementni qaytaradi.
import random
mevalar =['Olma','Anor','Shaftoli']
print(random.choice(mevalar))

car1=['Mitsubishi','Corvette C6.R','Porche 911 Carrera S']
print(random.choice(car1))


print("/////////////////////////////////////////////////// 8")
#                                          №8

# Usul choices()belgilangan ketma-ketlikdan tasodifiy tanlangan element bilan ro'yxatni qaytaradi.
import random
mevalar =['Olma','Anor','Shaftoli']
print(random.choices(mevalar))

mevalar =['Olma','Anor','Shaftoli']
print(random.choices(mevalar,weights=[5,1,3],k=14))


print("/////////////////////////////////////////////////// 9")
#                                          №9

# Usul shuffle()ro'yxat kabi ketma-ketlikni oladi va elementlarning tartibini qayta tashkil qiladi.
import random
mevalar =["'Olma","Anor","Shaftoli"]
random.shuffle(mevalar)
print(mevalar)


print("/////////////////////////////////////////////////// 10")
#                                          №10

# Usul sample()ketma-ketlikdan tasodifiy tanlangan elementlarning belgilangan soni bilan ro'yxatni qaytaradi.
import random
mevalar =['Olma','Anor','Shaftoli']
print(random.sample(mevalar,3))
print(random.sample(mevalar,k=2))


print("/////////////////////////////////////////////////// 11")
#                                          №11
# Usul random()0 dan 1 gacha bo'lgan tasodifiy suzuvchi raqamni qaytaradi.
import random
print(random.random())


print("/////////////////////////////////////////////////// 12")
#                                          №12
# Usul uniform()ikkita belgilangan raqam (ikkalasi ham kiritilgan) o'rtasida tasodifiy suzuvchi raqamni qaytaradi.
import random
print(random.uniform(10,20))
print(random.uniform(0,11))


print("/////////////////////////////////////////////////// 13")
#                                          №13
# Usul triangular()ikkita belgilangan raqam (ikkalasi ham kiritilgan) o'rtasida tasodifiy suzuvchi raqamni qaytaradi, lekin siz uchinchi parametrni, mode parametrni ham belgilashingiz mumkin.
import random
print(random.triangular(0,25))
print(random.triangular(0,20, 10))
print(random.triangular(0,25, 7))


print("/////////////////////////////////////////////////// 14")
#                                          №14
# Beta taqsimoti asosida 0 dan 1 gacha bo'lgan tasodifiy float sonini qaytaradi (statistikada ishlatiladi)
# import random
# print(random.binomialvariate(x))


print("/////////////////////////////////////////////////// 15")
#                                          №15
# Eksponensial taqsimotga asoslangan tasodifiy float sonini qaytaradi (statistikada ishlatiladi)
print(random.expovariate(5))#0.21914679045720536 ?
print(random.expovariate(0.5))#7.02263107345134 ?


print("/////////////////////////////////////////////////// 16")
#                                          №16
# Gamma taqsimotiga asoslangan tasodifiy float sonini qaytaradi (statistikada ishlatiladi)
print(random.gammavariate(1,10))
print(random.gammavariate(10,1))


print("/////////////////////////////////////////////////// 17")
#                                          №17
# Gauss taqsimotiga asoslangan tasodifiy float sonini qaytaradi (ehtimol nazariyalarida qo'llaniladi)
print(random.gauss(0,100))
print(random.gauss(11,2))


print("/////////////////////////////////////////////////// 18")
#                                          №18
# Log-normal taqsimotga asoslangan tasodifiy float sonini qaytaradi (ehtimol nazariyalarida qo'llaniladi) ?
# print(random.lognormvariate(1,100,)
#       print(50)


print("/////////////////////////////////////////////////// 19")
#                                          №19
# Oddiy taqsimotga asoslangan tasodifiy float sonini qaytaradi (ehtimol nazariyalarida qo'llaniladi)
print(random.normalvariate(0,1))
print(random.normalvariate(10,1))#11.183040960034027 ?


print("///////////////////////////////////////////////////\ 20")
#                                          №20
# Von Mises taqsimotiga asoslangan tasodifiy float sonini qaytaradi (yo'nalish statistikasida foydalaniladi)
print(random.vonmisesvariate(1,100))
print(random.vonmisesvariate(10,1))


print("///////////////////////////////////////////////////\ 21")
#                                          №21
# Pareto taqsimotiga asoslangan tasodifiy float sonini qaytaradi (ehtimol nazariyalarida qo'llaniladi)
print(random.paretovariate(100))
print(random.paretovariate(-10))


print("///////////////////////////////////////////////////\ 22")
#                                          №22
# Weibull taqsimotiga asoslangan tasodifiy float sonini qaytaradi (statistikada ishlatiladi)
print(random.weibullvariate(1,100))
print(random.weibullvariate(10,1))#17.372345412890308 ?