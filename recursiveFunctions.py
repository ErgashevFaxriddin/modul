# def countdown(n):
#     print(n)
#     if n == 0:
#         return
#     else:
#         countdown(n -1)
        
# countdown(100)

# ____________________________________________
# factorial
# def factorial(son):
#     print(son)
#     if son == 1:
#         return 1
#     else:
#         return son * factorial(son-1)

# print(factorial(10))

# ________________________________________________
# # fibonacci
# def fibonacci(son):
#     if son == 0:
#         return 0
#     elif son == 1:
#         return 1
#     else:
#         return fibonacci(son -1) + fibonacci(son-2)
    
# print(fibonacci(30))
# _________________________________________________________
# def fibonaccioptimal(son, cache={}):
#     if son in cache:
#         return cache[son]
#     if son == 0:
#         return 0
#     elif son == 1:
#         return 1
#     else:
#         result = fibonaccioptimal(son-1) + fibonaccioptimal(son-2)
#     cache[son] = result
#     return result

# print(fibonaccioptimal(991)) #max argument
# _________________________________________________________________
# numbers = [9, 4, 3, 5, 1, 7, 2, 8, 6]
# numbers.sort()
# print(", ".join(map(str, numbers)))
# ___________________________________________________
# # quck sort
# def quick_sort(lst):
#     if len(lst) <= 1:
#         return lst
#     else:   
#          pivot = lst[0]
#          left = [x for x in lst[1:] if x <= pivot]
#          right = [x for x in lst[1:] if x > pivot]
#          return quick_sort(left) + [pivot] + quick_sort(right)

# print(quick_sort([3, 4, 7, 5, 5, 8, 2, 9]))
# _____________________________________________________
# # GAME - tower of hanoi
# def hanoi(n, start, auxiliary, end):
#     if n == 1:
#         print(f"{start} → {end}")
#     else:
#         hanoi(n-1, start, end, auxiliary)
#         print(f"{start} → {end}")
#         hanoi(n-1, auxiliary, start, end)

# hanoi(3, "A", "B", "C")

print('Mehmonxonamizga xush kelibsiz!')
print('Buyruqni tanlang')
print('1 - mehmon qo\'shish',
      "2 - mehmonni olib tashlash",
      "3 - mehmonlar ro'yxati \n")
print('0 - dasturdan chiqish')

# ro'yxat ma'lumotlari ba'zasi
database = {
    "Ali": [1, 'standard'],
    'Temur': [7, 'lyuks']
}

# bosh bolmagan xonani tekshiruvchi funksiya
def check(data, key, value):
    for k, v in data.items():
        if str(v[key]) == str(value):
            return True
    return False

def plus():
    name = input('Ism: ')
    while name in database.keys():
        print('Bunday ismli mehmon mavjud!')
        name = input('Ism: ')
    number = input('Xona raqamini kiriting: ')
    while check(database, 0, number):
        print('Bu xona band, boshqa xona tanlang! ')
        number = input('Xona raqamini kiriting: ')
    def get_room_type():
        try:
            typee = input('Xona turini quyidagi belgilar orqali tanlang: \n e - ekonom \n s - standard \n l - lyuks \n ')
            if typee == 'e':
                return 'ekonom'
            elif typee == 's':
                return 'standard'
            elif typee == 'l':
                return 'lyuks'
            else:
                print('Xato belgi kiritildi!')
                return get_room_type()
        except Exception:
            print('Xato belgi kiritildi!')
            return get_room_type()
    room_type = get_room_type()
    database[name] = [number, room_type]
    print(f"{name} ro'yxatga qo'shildi \n \n")

# royxatdan olib tashlash funksiyasi
def minus():
    x = input('Kim mehmonxonadan ketmoqchi? ')
    if x in database.keys():
        database.pop(x)
        print(x, "Ro'yxatdan chiqarildi")
    else:
        print("Foydalanuvchi mavjud emas \n \n")
        
# royxatni korsatish funksiyasi
def show():
    print("{:<18} {:<25} {:<20}".format('Ismi', 'Xonasi', 'Xona turi'))
    print("-" * 50)
    for k, v in database.items():
        print("{:<18} {:<25} {:<20}".format(k, v[0], v[1]))
    print('\n')

# toliq jarayon uchun algoritm
while True:
    option = input(
        "Mehmonxonamizga xush kelibsiz! \n Buyruqni tanlang: \n 1 - mehmon qo'shish \n 2 - mehmonni ro'yxatdan olib tashlash \n 3 - ro'yxatni ko'rish \n \n 0 - dasturni to'xtatish\n>>> "
    )
    if option == '1':
        plus()
    elif option == '2':
        minus()
    elif option == '3':
        show()
    elif option == '0':
        print("Dastur to'xtatildi.")
        break
    else:
        print("Noto'g'ri buyruq! Qaytadan urinib ko'ring.\n")
    

# print('Mehmonxonamizga xush kelibsiz!')
# print('Buyruqni tanlang:')
# print('1 - Mehmon qo\'shish')
# print('2 - Mehmonni olib tashlash')
# print("3 - Mehmonlar ro'yxati")
# print('0 - Dasturdan chiqish\n')

# # Mehmonlar ro'yxati
# database = {
#     "Ali": [1, 'standard'],
#     'Temur': [7, 'lyuks']
# }

# # Xonani bandlikka tekshiruvchi funksiya
# def check(data, value):
#     for v in data.values():
#         if str(v[0]) == str(value):  # xona raqamini solishtiramiz
#             return True
#     return False

# # Mehmon qo'shish funksiyasi
# def plus():
#     name = input("Ism: ")
#     while name in database.keys():
#         print("Bunday ismli mehmon mavjud!")
#         name = input("Ism: ")

#     number = input("Xona raqamini kiriting: ")
#     while check(database, number):
#         print("Bu xona band, boshqa xona tanlang!")
#         number = input("Xona raqamini kiriting: ")

#     def get_room_type():
#         typee = input("Xona turini belgilang: \n e - ekonom \n s - standard \n l - lyuks \n>>> ")
#         if typee == 'e':
#             return 'ekonom'
#         elif typee == 's':
#             return 'standard'
#         elif typee == 'l':
#             return 'lyuks'
#         else:
#             print("Xato belgi! Qaytadan urinib ko'ring.")
#             return get_room_type()

#     room_type = get_room_type()
#     database[name] = [int(number), room_type]
#     print(f"{name} ro'yxatga qo'shildi!\n")

# # Mehmonni ro'yxatdan chiqarish funksiyasi
# def minus():
#     name = input("Kim mehmonxonadan ketmoqchi? ")
#     if name in database:
#         database.pop(name)
#         print(f"{name} ro'yxatdan chiqarildi!\n")
#     else:
#         print("Bunday foydalanuvchi yo'q!\n")

# # Mehmonlar ro'yxatini chiqarish funksiyasi
# def show():
#     print("{:<15} {:<10} {:<10}".format("Ismi", "Xonasi", "Xona turi"))
#     print("-" * 35)
#     for k, v in database.items():
#         print("{:<15} {:<10} {:<10}".format(k, v[0], v[1]))
#     print()

# # Asosiy menyu
# while True:
#     option = input("Buyruq tanlang (1, 2, 3, 0): ")
#     if option == '1':
#         plus()
#     elif option == '2':
#         minus()
#     elif option == '3':
#         show()
#     elif option == '0':
#         print("Dastur to'xtatildi.")
#         break
#     else:
#         print("Noto'g'ri buyruq! Qaytadan urinib ko'ring.\n")
