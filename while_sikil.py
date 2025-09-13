# while True:
#     setofor=input("Setafor qaysi rangda? ")
#     if setofor.lower() == "qizil" and "sariq" and "yashil" :
#         break
from Tools.scripts.objgraph import file2def




#                                                    2




# import random
#
# def guess_game():
#     opportunities = 10
#     rand = random.randrange(1, 10)
#     while opportunities > 0:
#         num = int(input("son kiriting: "))
#         if num == rand:
#             print("Tabriklaymiz! to'g'ri javob")
#             break
#         elif num > rand:
#             print("Biz o'ylagan son siz o'ylagan sondan kichik")
#         elif num < rand:
#             print("Biz o'ylagan son siz o'ylagan sondan katta")
#         opportunities -= 1
#     else:
#         print("Imkonyatingiz tugadi!")
#     return f"Bot taxmin qilgan son: {rand}"
#
# print(guess_game())





#                                               3
# ismlar = []
# while True:
#     dostlar = input(f" Dostlaringiz ismlarini kirizing\n Agr sikilni toxtatmoqchi bolsangiz 'stop' deb yozing:\n>>> ")
#     ismlar.append(dostlar.title())
#     if dostlar == "stop":
#         break
#
# print(ismlar)




#                                              4


# usd = 12.437
# print(f"1$={usd}")
# uzs= 0.00008
# print(f"12600so\'m={uzs}")
# while True:
#     savol = input(f"\nAgar dollor kursini hisoblomoqchi bolsangiz ($) kiriting\nAgar UZS kursini bilmoqchi bolsangiz (uzs) kiriting\n>>> ")
#     if savol.lower() == "usd":
#         qiymat = int(input("Qiymant kiriting: "))
#         print(float((usd*qiymat)))
#     # elif input("yana davom etishni hohlaysizimi ha / yoq") == "yoq":
#     #     break
#     if savol.lower() == "uzs":
#         qiymat2 = int(input("Qiymant kiriting: "))
#         print(float((qiymat2*uzs)))
#     if input("Yana dovom etishni hohlaysizmi ? ha/yoq: ").lower() == 'yoq':
#         break
