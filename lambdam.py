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

sonlar = [1, 2, 3]
kvadratlar = list(map(lambda son: son **2, sonlar))
print(kvadratlar)