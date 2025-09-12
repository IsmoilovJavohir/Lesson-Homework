# ob_havo = int(input("Bugun ob-havo harorati qanday?\n>>> "))
# if ob_havo < 0:
#     print("Sovuq kun")
# elif ob_havo < 20:
#     print("salqin kun")
# elif ob_havo < 30:
#     print("Iliq kun")
# else:
#     print("Juda issiq kun")

#                                         2

# chegirma = int(input("Chegirma olish uchun harid qilgan mahsulotlaringizni jammiy sumasini kirgazing \n>>>"))
# if chegirma < 50000:
#     print("afsus agar 50,000somdan oshiq mahsulot harid qilsangiz chegirmalarimiz mavjud")
# elif chegirma < 100000:
#     print("5% chegirma")
# else:

# harid= int(input("Haridingiz jamiy qancha boldi? "))
# if harid > 50000:
#     print(f"Sizdan jamiy {harid}")
#
# elif harid< 50000:
#     chegirma = 5
#     chegirma_A = harid * (chegirma / 100)
#     jamiy= harid -chegirma_A
# print(f"jamiy {jamiy}")
#                                                      3

# login = input("login,ingizni kiriting: ")
# parol = input("iltimos login,ingz parolini kirgazing: ")
# if login == "admin" and parol == "12345":
#     print("Xush kelibsiz, admin!")
# else:
#     print("Login yoki parol xato")
#                                                       4

# yosh = int(input("Yoshingiz qanchada? "))
# if yosh < 13:
#     print("Sizga ushbu film tavsiya etilmaydi")
# elif yosh < 17:
#     print("Siz filmni ota-onangiz bilan ko'rishingiz mumkin")
# else:
#     print("Siz filmni tomosha qilishingiz mumkin")
#                                                       5


# menu  = input("Qanday taom yeyishni hohlaysiz\n\nMENU \n1.osh\n2.mastava\n3.shashlik\n>>>")
# menu_o = ["osh","mastava","shashlik"]
# menu_o= menu
# if menu_o.lower() == "osh":
#     print(f"{menu_o}-35.000 som 15 daqiqada tayor boladi")
# elif menu_o.lower() == "mastava":
#     print(f"{menu_o}-30.000 som\n 20 daqiqada tayor boladi")
# elif menu_o.lower() == "shashlik":
#     print(f"{menu_o} 10.000 som\n10 daqiqada tayor boladi")
# else:
#     print("bizda faqat menu dagi taomlar mavjud")
#                                                      6

# login=input("Iltimos email manzilingizni kiriting\n>>> ")
# if login.find("@") == -1:
#     print(f"{login} Notogri email manzili")
# elif login.find(".") == -1:
#     print(f"{login} Notogri email manzili")
# else:
#     print(f"{login} Xush kelibsiz mg jin")
#                                                      7
# baho = int(input("qancha ball oldingiz "))
# if baho < 55:
#     print("2 baho")
# elif baho <69:
#     print('3 baho')
# elif baho < 85:
#     print('4 baho')
# else:
#     print('5 baho')

#                                                      8

# kartadagi_p = int(input("Kartaingizda qancha mablagingiz bor: "))
# yechish = int(input("qancha som yechmoqchi siz: "))
# if kartadagi_p < yechish:
#     print("Hisobda yetarli mablag' mavjud emas")
# elif yechish < 5000:
#     print("Minimal yechish summasi 5 000 so'm")
# else:
#     print(f"Pul muvaffaqiyatli yechildi qoldiq: {kartadagi_p-yechish} som")


#                                                       9

# kunlar_royxati = ["Yakshanba", "Dushanba", "Seshanba", "Chorshanba", "Payshanba", "Juma", "Shanba"]
# print(kunlar_royxati)
# kun = input("bugun qaysi kun?\n>>> ").lower()
# if kun == "shanba" and "yakshanba":
#     print("Bugun dam olish kuni")
# elif kun == "dushanba" and "seshanba" and "chorshanba" and "payshanba" and "juma":
#     print("Bugun ish kuni")
# else:
#     print("Imlo xota! Iltimos kunlarni aniq yozing")

#                                                         10

# savol = int(input("Foydalanuvchidan oyiga qancha internet trafikidan foydalanasiz ? \n>>> "))
# if savol <= 1:
#     print(f"{savol}GB Sizga 'Mini' tarifi mos keladi")
# elif savol <= 5:
#     print(f"{savol}GB Sizga 'Standard' tarifi mos keladi")
# elif savol > 5:
#     print(f"{savol}GB Sizga 'Unlimited")
# else:
#     print(f"Faqat foydalanmoqchi bolgan GB sonini kiritsangiz bas ")