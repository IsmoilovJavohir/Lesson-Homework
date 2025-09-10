#.append rohat ohiriga bita yangi element qoshadi
# mevalar= ["olma","banan","anor"]
# mevalar.append("shaftoli")
# print(mevalar)
# #faqat bita!
# sonlar=[1,2,3]
# sonlar.append([4,5,6])
# print(sonlar)

 #.clear()- bu metod list ichidagi hma elementlarni ochirib yuboradi
# mevalar=["uzum","olma","anor"]
# mevalar.clear()
# print(mevalar)
# raqamlar=[1,2,3,4,5]
# raqamlar.clear()
# # raqamlar.append(6)
# print(raqamlar)


#.copy()- bu lest ichidagi malumotlarni nuxsalaydi va asl lestga tegmaydi
# mevalar=["olma","anor","gilos"]
# new_mevalar=mevalar.copy()
# a=new_mevalar.append("shaftoli")
# print("asl",mevalar ,a)
# print("nuxsalangan",new_mevalar)


#royhatda berilgan element necha marta qatnashganini sanaydi
# mevalar =["olma", "glos", "olma","anor", "olma"]
# print(mevalar.count("olma"))
# raqamlar=[1,2,2,3,3,52,2,5,]
# print(raqamlar.count(2))

#.extend- elementlarni boshqa list,ga bir-mabir qoshadi (.append()-ga ohshab lekin birmabir=[1,2,3,[4,5]] )
# mevalar=['olma',"glos","uzum"]
# mashinalar=["maluba","Jentira","matiz"]
# mevalar.extend(mashinalar)
# print(mevalar)
#
# sonlar=[1,2,3]
# hariflar=["a","b","c"]
# sonlar.extend(hariflar)
# print(sonlar)

#index()- berilgan elementni royhat ichidan birinchi uchraganini index qaytaradi  "index-0 dan boshlab sanaydi!"
#                        !
# mevalar=["olma","anor","olma","uzum"]
# print(mevalar.index("olma"))
# #          !
# raqamlar=1,2,3,4,5,2
# print(raqamlar.index(2,2))


#insert()- royhatni malum bir joyiga yangi element qoshadi

# mevalar=['olma',"anor","uzum"]
# mevalar.insert(1,"shaftoli")
# print(mevalar)
#
# mevalar=['olma',"anor","uzum"]
# mevalar.insert(4,2)
# print(mevalar)

# pop()- elementni ochiradi va ochirilgan elementni qaytaradi
# mevalar=["olma","anor","gilos"]
# ochirilgan=mevalar.pop(1)#agar index berilmasa oxirgi elementni ochiradi(0)
# print("list", mevalar,"ochirilgan element-", ochirilgan)

# .remove()- royxatda birinchi uchuragan elementni ochiradi undan keyin qatnashgan ikkichi elementga tegmaydi
# mevalar=["anor","uzum","olma","anor"]
# mevalar.remove("anor")#agar element yoq bolsa error chiqaradi
# print(mevalar)


# #royxat elementlarini teskari joylashtiradi
# mevalar= ["olma", "anor","shaftoli" ]
# mevalar.append("o'rik")
# mevalar.reverse()
# print(mevalar)

#sort()- elementlarni ketma-ketligda tartib leydi
# sonlar = [2,5,6,8]
# sonlar.sort()
# print(sonlar)