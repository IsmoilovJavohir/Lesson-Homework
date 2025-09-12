# a= {1, 2, 3}
# a.add(5)#yangi element qoshadi (agar bola gan bolsa)
# print(a)
#
# #clear()- set ichidagi barcha elementlarni ochiradi
# a= {1, 2, 3}
# # b= {4, 5, 6}
# c= a.clear()
# print(a.add(1))
#
# #union()- set ichidagi elementlarni birbiriga qoshib yuboradi
# a= {1, 2, 3}
# b= {5,6,7}
# a=b.union(a)
# print(a)
#
# #intersection()-ikkita set ichidagi elementni qidiradi (5)
# a= {5, 2, 3}
# b= {5,6,7}
# d=a.intersection(b)
# print(d)
#
# # difference()-w3schools dagi manosina chunmadim manimcha aichindagi eleementlani b ga otiri baradi
# a= {1, 2, 3}
# b= {5,6,7}
# e=a.difference(b)
# print(e)
#
# #symmetric_difference()-ikkkala element birlashmasini oz ichiga oladi
# a= {1, 2, 3}
# b= {5,6,7}
# f = a.symmetric_difference(b)
# print(f)
#
# #update()-Agar ikkala to'plamda ham element mavjud bo'lsa, yangilangan to'plamda ushbu elementning faqat bitta ko'rinishi mavjud bo'ladi.
# a= {1, 2, 3}
# b= {5,6,7}
# b.clear()
# a.update(b)
# print(a)
#
# #discard()- korsatilgan elementni olib tashlaydi agar korsatilgan element topolmasa error bermaydi
# a= {1, 2, 3}
# b= {5, 6, 7}
# a.discard(3)
# print(a)
#
# #remove()- agar berilgan eelementni topolmasa error qaytaradi
# a={1, 2, 3}
# a.remove(4)
# print(a)

#issubset()-set ichida korsatilgan element mavjud bolsa True agar mavjud bolmasa False
# a={"salom dunyo"}
# b={1,2,3}
# l= b.issubset(a)
# print(l)
#
# #issuperset()- set ichiga korsatilgan element mavjud bolsa True agr vajud bolmasa False
# k= b.issuperset({1,2})
# print(k)
#
#
# #isdisjoint()-ikkala to'plamda elementlardan hech biri mavjud bo'lmasa, True qiymatini aks holda u False qiymatini qaytaradi.
# a={1,2,3,4,5}
# b={4,5,6,7}
# j= a.isdisjoint(b)
# print(j)
#
# #pop()- set ichidagi birinchi elementni olib tashlaydi
# a={1,2,3,4,5}
# b={"banana","apple","shaftoli"}
# a.pop()
# b.pop()
# print(a,b)

