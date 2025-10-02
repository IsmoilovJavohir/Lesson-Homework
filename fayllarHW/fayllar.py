import pickle

with open('pi_million_digits.txt', 'r') as million:
    a = million_digits = million.read()
tekshirish = a.count('20092006')
if tekshirish > 0:
    print(".txt ichida 20.09.2006 raqami mavjud")
else:
    print("izlaniyotgan raqam topilmadi")#agar 20.09.20 raqamini izlaganimda True bolar adi

