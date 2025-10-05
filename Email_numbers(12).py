import  re
andoza_emil = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'

emails = [
    "ali@gmail.com",  # ✓ To'g'ri
    "test.user@yahoo.uz",  # ✓ To'g'ri
    "invalid@",  # ✗ Noto'g'ri
    "@example.com",  # ✗ Noto'g'ri
    "user@domain"  # ✗ Noto'g'ri
]
for email in emails:
    if re.match(andoza_emil, email):
        print(f"{email}✓ To'g'ri")
    else:
        print(f"{email}✗ Noto'g'ri")



andova_tel = '^[\+]{1}[(]?[998]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$'
while True:
    telifon_n = input('Telifon raqamingizni kiriting:')
    if re.match(andova_tel, telifon_n):
        print(f"Qabul qilindi: {telifon_n}")
        break
    else:
        print(f"Biz faqat O'zbekiston raqamlarini (+998) qabul qilamiz.")