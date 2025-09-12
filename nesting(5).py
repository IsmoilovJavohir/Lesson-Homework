# metodlar= {
#     'boolean':'Boolean-Mantiqiy qiymat',
#     'float':'Float-O\'nlik son',
#     'for':'For-Bironbir amalni qayta-qayta bajarish tsikli',
#     'if':'If-Shartlarni tekshirish operatori',
#     'integer':'Integer-Butun son'
# }
# for med,txt in metodlar.items():
#     print(txt)
# print("                              ")
# davlatlar_p = {"AQSH":"Bishkek",
#                "ITALIYA":"Dushanbe",
#                "MALAYZIYA":"Kuala-Lumpur",
#                "O\'ZBEKISTON":"Moskva",
#                "QIRG\'IZISTON":"Nursultan",
#                "QOZOG\'ISTON":"Rim",
#                "ROSSIYA":"Sungapur",
#                "SINGAPUR":"Toshkent",
#                "TOJIKISTON":"Washington D.C"
# }
# for davlat in sorted(davlatlar_p.keys()):
#     print(f"Dunyo davlatlari\n{davlat}")#hamasini printda upper atish mumkinliki keyin yoda chuchdi
# for poytaxt in sorted(davlatlar_p.values()):
#     print(f"Poytaxtlar {poytaxt}")
# print("       ")




# savol= input("qaysi davlatlat poytaxtini bilishni hohlaysiz?\n>>>")
# if savol.lower() == "aqsh":
#     print(f"{savol.upper()} poytaxti Washington D.C")
# elif savol.lower() == "rossiya":
#     print(f"{savol.upper()} poytaxti Moskva")
# # va h\k
# else:
#     print(f"Kechirasiz bida bu {savol} haqida malumot yoq")

# kinolar={}
# ism_1 = input("Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali nima?\nIsmi: ")
# kino_1 = input("1-kino nomini yozing: ")
# kino_2 = input("2-kino nomini yozing: ")
# kino_3 = input("3-kino nomini yozing: ")
# # kinolar ={}
# kinolar[ism_1]=[kino_1,kino_2,kino_3]
#
# ism_2 = input("Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali nima?\nIsmi: ")
# kino_4 = input("1-kino nomini yozing: ")
# kino_5 = input("2-kino nomini yozing: ")
# kino_6 = input("3-kino nomini yozing: ")
# # kinolar_2 ={}
# kinolar[ism_2]=[kino_4,kino_5,kino_6]
#
# ism_3 = input("Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali nima?\nIsmi: ")
# kino_7 = input("1-kino nomini yozing: ")
# kino_8 = input("2-kino nomini yozing: ")
# kino_9 = input("3-kino nomini yozing: ")
# # kinolar_2 ={}
# kinolar[ism_2]=[kino_4,kino_5,kino_6]
# for ism_1,kinolar_royxati in kinolar.items():
#     print(f"{ism_1.title()} yoqtirgan 3-ta film: {kinolar_royxati}")
#
# for ism_2,kinolar_royxati in kinolar.items():
#     print(f"{ism_2.title()} yoqtirgan 3-ta film: {kinolar_royxati}")
#
# for ism_3, kinolar_royxati in kinolar.items():
#     print(f"{ism_3.title()} yoqtirgan 3-ta film: {kinolar_royxati}")
# xatola! 1#kinolar ozgaruvchisini qayta-qayta ishlatgani #2for & .items dan foydalamaganim 3#print da list atib chiqarish uchun 1 sat vaqt yoqatishim 4#printa boshqacha chiqraman dab adashib getganim -2soat
# ', '.join()- fishka ','bilan yoqnarsani chaqirib keyin qavus ichina ozinga garak narsani maslam keye,ozgaruvchiga hohlagan metodingi ishlatsang boladi akan



uzb={
    'malumot':'O\'zbekistonning poytaxti Toshkent',
    'hududi':'448978 kv .km',
    'aholisi':'33000000',
    'pul birligi':'som'
}
rus={
    'malumot':'Rossiyaning poytaxti Moskva',
    'hududi':'17098246 kv .km',
    'aholisi':'144000000',
    'pul birligi':'rubl'
}
usa= {
      'malumot':'AQSHing poytaxti Vashington',
      'hududi': '9631418 kv.km',
      'aholisi':'327000000',
      'pul birligi':'dollar'
}
malayiza={
    'malumot':'Malayziyanning poytaxti Kuala-Lumpur',
    'hududi': '329750 kv .km',
    'aholisi':'25000000',
    'pul birligi':'ringngit'
}

davlatlar=[uzb,rus,usa,malayiza]
for davlat in davlatlar:
    print(f"{davlat['malumot'].title()}\n"
          f"Hududi: {davlat['hududi']}\n"
          f"Aholisi: {davlat['aholisi']},\n"
          f"Pul birligi: {davlat['pul birligi']}\n")