# pochtalar = ["user1@gmail.com", "user2yahoo.com", "user3@outlook.com"]
# for pochta in pochtalar:
#     if "@" in pochta:
#         print(f"qabul qilingan {pochta}")
#     else:
#         print(f"Notogri! {pochta}")



#                                                    2
# parollar=["password123", "Qwerty!", "admin", "StrongPass1!"]
# for parol in parollar:
#     if len(parol) <7 :
#         print(f"{parol} 8ta harifdan kam bolmasligi kerak")
#     elif parol.islower() == True or parol.isalpha() != True :
#          print(f"{parol} belgilar bolmagani yoki sonlar bolmaganligi uchun kuchsiz porol")
#     # else:
#     #     print(f"{parol} kuchli parol")



#                                                   3
# ob_havo = [20,22, 19, 24, 25, 23, 21]
# kun= "yakshanba","dushanba","seshanba","chorshanba","payshanba","juma","shanba"
# a=19+25
# b=a/2
# # ob_havo.sort()
# for havo,kun in zip(ob_havo,kun):
#     if havo >= b:
#         print(f"Iliq kun-{kun} {havo}")
#     else:
#         print(f"Salqin kun-{kun} {havo}")



#                                                     4
# mavjud_t = ["manti", "osh", "shashlik","lag\'mon"]
# buyurtma = input("Qanday taom tanavul qilishni hohlaysiz?\n>>>")
# for menu in mavjud_t:
#     if buyurtma.lower() == menu:
#         print(f"{buyurtma.title()}: Buyurtma qabul qilindi")
#     else:
#         print(f"{buyurtma}: Kechirasiz bizda bunday taom mavjud emas\n Hozirda mavjud bolgan toamlar: {mavjud_t}")




#                                                    5

# foydalanuvchilar_yoshi = [16, 21, 17, 30, 25]
# foydalanuvchilar = ["Ali","Joxa","Vali","Javohir","Atham"]
# for yoshi, ismlar in zip(foydalanuvchilar_yoshi, foydalanuvchilar):
#     if yoshi <= 18:
#         print(f"{ismlar}Yosh chegarasiga yetmagan")
#     else:
#         print(f"{ismlar} Xush kelib siz")



#                                                     6

# xabarlar = ["Yangi xabar", "Batareya past", "Yangilanish mavjud"]
# eslatish = ["Sizga **** yurakcha bosdi", "Telifoningizni quvatlang!", "Yangi One UI yangilanish keldi"]
# for xabar, eslatma in zip(xabarlar, eslatish):
#     if Yangi xabar



#                                                       7

# fayllar = ["kitob.jpg", "ko_jiguli.mp3", "tabiat.jpg", "malohat.mp3", "iphone.jpg"]
# rasimlar =[]
# musiqalar=[]
# for fayl in fayllar:
#     if '.jpg' in fayl:
#         rasimlar.append(fayl)
#     else:
#         musiqalar.append(fayl)
# print(rasimlar, musiqalar)