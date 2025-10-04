import json

JSON = {"model" : "Malibu", "rang" : "qora", "yil":2020, "narh":40000}
faylnomi = 'car.json'
with open(faylnomi,'w') as fayl:
    fayl.write(json.dumps(JSON))
with open(faylnomi, 'r') as file1:
    salom = json.load(file1)
print(f"Malumot: {salom['model']} Rangi:{salom['rang']} yili-{salom['yil']} Narh: {salom['narh']}.som ")



talaba_json = {"ism" : "Hasan" , "familiya" : "Husanov" , "tyil" : 2000}
ozgaruvchi = 'talaba.json'
with open(ozgaruvchi,'w') as talaba:
    talaba.write(json.dumps(talaba_json))

with open(ozgaruvchi, 'r') as talaba:
    data = json.load(talaba)
print(f"Talaba: {data['ism']} {data['familiya']} {data['tyil']}-tug'uli")


talabalar = 'students.json'
with open(talabalar,'r') as json_talabalar:
    box = json.load(json_talabalar)
    for sikil in box['student']:
        print(f"Ismi:{sikil['name']} Familiyasi:{sikil['lastname']} Bosqich-{sikil['year']}  Yonalishi:{sikil['faculty']}")