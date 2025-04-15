# # LAMBDA
# ozgaruvchi = lambda argument: argument *2
# print(ozgaruvchi(2))

# birinchison = int(input('1-son: '))
# ikkinchison = int(input('2-son: '))

# kopaytir = lambda birinchison, ikkinchison: birinchison * ikkinchison
# natija = kopaytir(birinchison, ikkinchison)
# print(f"natija: {natija}")

# #map() funksiyasining vazifasi – har bir elementga lambda funksiyasini qo‘llash. 
# Agar map() bo‘lmasa, lambda faqat bitta qiymatni qaytaradi, butun ro‘yxatni emas.

# sonlar = [1, 2, 3]
# kvadratlar = list(map(lambda son: son **2, sonlar))
# print(kvadratlar)

# # ✅ Berilgan sonning kvadratini hisoblaydigan lambda funksiyasini yozing.
# while True:
#     son = input('son: ')
#     if son == 'x':
#         break
#     if son:
#         kvadrat = lambda x: x **2
#         print(f"quadrate of {son} is {kvadrat(int(son))}")
#     else:
#         print('raqam kiriting: ')
#         continue

# kvadrat = lambda x: x **2
# print(kvadrat(3))

# multiply = lambda x, y: x * y
# print(multiply(2, 5))

# # ikkita argument qabul qilish
# divide = lambda bolinuvchi, boluvchi: int(boluvchi) / int(bolinuvchi)
# print(divide(10, 5))

# juftmi = lambda son: "juft" if son % 2 == 0 else "toq"
# print(juftmi(5))

# qoshish = lambda x, y : x + y
# natija = qoshish(2, 10)
# print(natija)

# # sonlarni 3 barobarga oshirish
# sonlar = [1, 4, 10]
# yangisonlar = list(map(lambda son: son * 3, sonlar))
# print(yangisonlar)

# from math import sqrt

# sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yxati
# ildizlar = list(map(sqrt,sonlar))
# print(ildizlar)
# _________________________________________________________________
# sonlar = list(range(11))

# def daraja2(x):
#   return x*x

# print(list(map(daraja2, sonlar)))\
# _____________________________________________________________
# sonlar = list(range(11))
# kvadratlar = list(map(lambda x: x*x, sonlar))
# print(kvadratlar)
# _______________________________________
# sonlar = list(range(11))
# kvadratlar = []
# for son in sonlar:
#   kvadratlar.append(son)
# print(kvadratlar)
# _______________________________________
a = [4, 5, 6]
b = [7, 8, 9]
a_plus_b = list(map(lambda x,y:x+y,a,b))
print(a_plus_b)