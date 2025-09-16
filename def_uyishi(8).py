# def user_data (first_name, last_name, age):
#     """def salom_ber(ism):
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
#
# salom_ber('hasan') """
#     first_name = print(f"Ism: {first_name.title()}")
#     last_name = print(f"Familiya: {last_name.title()}")
#     age = print(f"Yosh: {age.title()}")
# user_data(input("Ism kiriting: "), input("Familiya: "), input("Yosh: "))
from operator import index


#                                                   //// 2  \\\\


# def find_max(a, b, c):
#     """Eng katta soni aniqlab beradi!"""
#     maximum = max(a, b, c)
#     print(maximum)
#     return maximum
#
# find_max(float(input("A,ga son kiriing: ")), float(input("B,ga raqam kirizing: ")), float(input("C,ga raqam kirgazing: ")))


#                                                ////  3  \\\\


# def find_letter_count(word, letter):  ##https://www.w3schools.com/python/trypython.asp?filename=demo_ref_string_count
#     """matin ichidan belgi izlovchi funksiya!"""
#     qaytaruvchi = word.count(letter)
#     print(qaytaruvchi)
#
# find_letter_count(input("matin kiriting: "), input("Matin ichidan qidirilishi kerak bolgan belgi: "))


#                                              ////  4   \\\\
# def list_sum(myList):
#     javob = sum(myList)
#     print(javob)
# list_sum([1,2,3,4,5])

#                                                ////  5  \\\\


# def daraja (a,b):
#     """a-sondan b-darajasini qaytaradi"""
#     print(f"{a**b}")
# daraja(float(input("Son kiriting: ")), float(input("Izlamoqchi bolgan darajangizni kiriting: ")))


#                                           ////  6  \\\\



# def daraja1 (a,b,c,d):
#     """berda * qoydim lekin darajasini hisob lab duribdi nn likini bilmiman?"""
#     print(f"{a*b}")#print(f"{a**b}")
#     print(f"{a*c}")#print(f"{a**c}")
#     print(f"{a*d}")#print(f"{a**d}")
#
# daraja1(float(input("Raqam kirizing: ")), float(input("Raqamni 1-darajasini kirtining: ")), float(input("Raqamni 2-darajasini kirtining: ")), float(input("Raqamni 3-darajasini kirtining: ")))


#                                         ////  7  \\\\
# def digit_count_and_sum(word):
#     sonlar=[]
#     for a in word:
#         if a.isdigit():
#             sonlar.append(int(a))
#     print(len(sonlar))
#     print(sum(sonlar))
# digit_count_and_sum("ab4s39h2")
# #                                         ////  8  \\\\
# def add_right(a, b):
#     add_right = str(a) + str(b)
#     print(int(add_right))
#
# add_right(5,8)
# #                                         ////  9  \\\\
# def add_left(a, b):
#     add_left= str(b) + str(a)
#     print(add_left)
#
# add_left(5,8)
#                                        ////  10  \\\\


# def work_with_list(a):
#     for yigindi in a:
#         box = min(a)
#         javob = box *yigindi
#         print(javob)
#
# work_with_list([2,8,4])


#                                      ////  11  \\\\


# def big_sales(sales=()):
#     """qaysi oyda engkop savdo qilinganini korsatuvchi funksiya!"""
#     sales={
#         "yanvar": 12000,
#         "mart": 6000,
#         "aprel": 15000,
#         "sentabr": 19000,
#         "dekabr":1000
#     }
#     return max(sales.values())
# print(big_sales())#!!!keys!!!


#                                        ////  12  \\\\ xato!
# def min_max(numbers, max_num=(), min_num=()):
#     max_son=max(numbers)
#     min_son=min(numbers)
#     if max_son==max_num:
#         print(f"Ha {max_num} engkatasi")
#     elif min_son==min_num:
#         print(f"Ha {min_num} kichiki")
#     else:
#         print(f"Yo\'q notogri {max_num}")
#         print(f"Yo\'q notogri {min_num}")
#
#
# min_max([3, 5, 9, 2],9,2)

#                                        ////  13  \\\\
# def expensiveProduct(products=()):
#     products={
#         "Iphone X": 600,
#         "Iphone 12": 1500,
#         "Samsung Note 9": 800,
#         "Samsung S10": 1100
#     }
#     # print(max(products.keys()))
#     return max(products.values()  )#or and products.keys())
# print(expensiveProduct())