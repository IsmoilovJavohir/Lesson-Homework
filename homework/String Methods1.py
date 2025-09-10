##capitalize() matin boshidagi harifni kata qilib beradi
# gap = "HeLLo WorLd" #N1
# print(gap.capitalize())
#
# gap = "siz kichkina SHAHZODA kitobini o'qiganmisiz" #N2
# print(gap.capitalize())
#
# gap = 'sizlar chiroyli ekansizlar, lekin sizlarda jon yo‘q... Hech kim sizlar uchun o‘lishga tayyor emas. Albatta, mening atirgulim ham sizlarga o‘xshab qaraganda oddiygina bir gul, lekin men u bilan do‘stlashdim — shuning uchun u noyob bo‘lib qoldi'
# print(gap.capitalize()) #Kichkina shahzoda kitobidan bir jumla (N3)
#
#
##casefold() matin,lardagi hariflarni barchasini kichiq qilib beradi
# gap = "STOP !"
# print(gap.casefold())
#
# gap = "MEN O'QIYAB MAN"
# print(gap.casefold())
#
# gap = "Okay MEME :)"
# print(gap.casefold())
from itertools import count

##center() bu matinlarni ortaga bosh joy yoki belgi*/# bilan surush uchun
# gap = "SAlom dunyo"
# print(gap.center(30))
#
# gap = 'SAlom dunyo'
# print(gap.center(20, "👾"))
#
# gap = '__width & __fillchar'
# print(gap.center(100))

## count() yordami bilan matindagi hohlagan jumla yoki matin ichida ishlatilgan belgini nechi marta ishlatilganini sanab beradi
# gap = "Agar muqaddas lashkar qichqirsa: ‘Tashla sen Rossiyani, jannatda yashagin!’ — Men aytaman: ‘Kerak emas menga jannat, qaytaring yurtimni"
# x = gap.count("jannat")
# print(x)
#
# gap = "Sergey Yesenin"
# A = gap. count("e",2,5)
# print(A)
#
# gap ="a1a2a3a4a5a6a7a8a9"
# PlusMnus = gap.count("a", -7,16)
# print(PlusMnus)

#encode() matinlarni b-(baytlarga) aylantirib-almashtirib beradi
# gap = 'Coffe ?☕'
# print(gap.encode("utf-8"))
#
# gap = "Hello World👾"#yozilishi boyicha xatolarni etiborsiz qoldiradi akan massalam emoje
# print(gap.encode("ascii", "ignore"))

# gap = "Ide qomadi"
# print(gap.encode("ascii", "ignore"))

# gap = 'Reklama:Fanta iching '
# print(gap.encode("ascii", "replace"))
#
# gap = "Hello(👾) World"
# print(gap.encode("ascii", "ignore"))
#
# gap = 'Hello(👾) World'
# print(gap.encode("ascii", "replace"))
# print(gap.encode("replace")) #ascii qoshmasdan ishlatib bolmas ekan

#endswith() matini ohiri belgilar bilan tugashini tekshirib beradi(!.exe.txt...)
# gap = 'kulib yur !'
# print(gap.endswith('!'))
#
# gap = "Samsung z flip4"
# print(gap.endswith("Samsung"))#agar 4 belgilaganimda true bolar adi
#
# gap = "NeedForSpeed.exe"
# print(gap.endswith("NeedForSpeed.exe"))#kata fayl,lar bilan ishlaganda as qotadi
#
# gap = "men Python oqiyabman "#matin nichik tomom bolishini aniqlab barami ? chunarsiz va foydasiz dab oyliman.
# print(gap.endswith(" "))

#expandtabs() matin ichida \t qoldirilib ketsa expandtabs()code yordamida joy ochish mumkin har bir tab 8space
# gap = "Hello\tWorld"
# print(gap.expandtabs())
#
# gap = "Hello\tWorld"
# print(gap.expandtabs(9))
#
# gap = 'A\tW\tC\tD'
# print(gap.expandtabs(8))

#.find matin ichidagi birin bir soz yoki belgini qidiradi
# gap = 'Slom dunyo Hello World'
# print(gap.find("dunyo"))
#
# gap = 'Slom dunyo Hello World'
# print(gap.find("duny0"))
#
# gap = "nothing nothing salom dunyo nothing nothing salom dunyo nothing nothing ctr+v"
# print(gap.find("salom dunyo",40,60))

 #.format bu string ichiga ozgarturuvchilar yoki qiymatlar bera olamiz
# gap = "mening ismim {} va men {}"
# print(gap.format("Javohir", "Cofee ichyab man"))
#
# gap = 'Javob 1.{0} 2-savolga Javob {1}'
# print(gap.format("(C)", "(B)"))
#
# gap= "Mening ismim {ism}, yoshim {yosh}"
# print(gap.format(ism="Javohir", yosh="99.09"))
#
# gap= "Bu oyoq kiyimi {} {} turadi"
# print(gap.format("128.000" , "$om"))

#format_map() farmatga ohshab ishlaydi lekin
# gap = "meniing {ism} yoshim {yosh}"
# info = {"ism": 'Javohir' ,"yosh":18}
# print(gap.format_map(info))
#
# from collections import defaultdict
# gap = "{ism} {yosh} {familiya} " #defaultdict bolmaganda xato berar edi defaultdict yordamida bu xatoni tuzatik yk ochiq qoldirib ketik
# info = defaultdict(str, {"ism": "Javohir", "familiya":"Ismoilov"})#str ishlatilsa bosh string qaytaradi va hato(error) orniga bosh spec chiqdi
# print(gap.format_map(info))
#
# matin = "{hayvon} uchadi, {hayvon} uchmaydi"
# info = {"hayvon": "ot"}
# print(matin.format_map(info))
#
# gap = "Hello {nima}"
# info = {"nima": "World"}
# print(gap.format_map(info))

#index() .find() ga ohshab ishlidi lekin berlgan malumotni topo olmasa (error) baradi akan
# gap = "Salom dunyo"
# print(gap.index("o"))
#
# # gap= "Alisher Navoiy"#6-chi pazitsiyada turibdi lekin boshqa joyni qidirsak .find()-ga oqshab -1 emas (error) berar ekan
# # print(gap.index("r",7,9))
#
# gap = "1234567890"#1234567890 str larni qidirmidi akan va 0 dan boshlab pazitsiya sonidi akan
# print(gap.index("6"))

#.isalpha matin ichida spec yoki son larni tekshirib beraddi agar spec yoki son qatnashgan bola false chiqaradi!
# gap = "Hello"
# print(gap.isalpha())
#
# gap = "Hello World"
# print(gap.isalpha())#folse sabbi matin ortasida spec bor
#
# gap = "Hello123"
# print(gap.isalpha()) #sonlar qatnashsa ham  folse
#
#
# gap = "Привет"
# print(gap.isalpha())
# #boshqa tilarda ham ishdi
# gap = "こんにちは"
# print(gap.isalpha())

# gap = "hello world"
# print(gap.isascii())
#
# gap = "hello world👾"
# print(gap.isascii())
#
# gap = "こんにちは"  # yaponcha va boshqa tilarni false sababi Aa-Zz gacha ture chiqaradi va sonva belgilar teue lekin emojelar false
# print(gap.isascii())

