def kvadrat():
    while True:
        son = input('son kiriting: ')
        if son1 == 'x'.lower():
            break
        if son.isdigit():
            print(f"{son}: {int(son) ** 2}")
        else:
            print("son kiriting, (x = exit)")
        
def kub():
    while True:
        print('kub hisoblovchi dastur')
        son = input('son: ')
        if son == 'x'.lower():
            break
        if son.isdigit():
            print(f"{son}: {int(son) ** 3}")
        else:
            print('son kiriting')
                    
def plus():
    while True:
        print('ikki sonni bir-biriga qoshuvchi dastur')
        son1 = input('1-son: ')
        if son1 == 'x'.lower():
            break
        son2 = input('2-son: ')
        javob = int(son1) + int(son2)
        print(javob)
        
def minus():
    while True:
        stop = 'x'
        print('ikki sonni bir-biridan ayiruvchi dastur')
        son1 = input('1-son: ')
        son2 = input('2-son: ')
        if stop:
            break
        javob = int(son1) - int(son2)
        print(f"{son1} - {son2} = {javob}")

def multiply():
    while True:
        print('ikki sonni ko\'paytiruvchi dastur')
        son1 = input('1-son: (x = exit) ')
        if son1.lower() == 'x':
            break
        son2 = input('2-son: ')
        if son1.isdigit() and son2.isdigit():
            print(f"{son1} x {son2} = {int(son1) * int(son2)}")
        else:
            print("Faqat son kiriting!")
            
def divide():
    while True:
        print('bir sonni ikkinchisiga boluvchi dastur\nStop: (x)')
        son1 = input('1-son: ')
        if son1.lower() == 'x':
            break
        if son1.isdigit():
            son2 = input('2-son: ')
            if son2.lower() == 'x':
                break
            if son2.isdigit():
                print(f"{son1} / {son2} = {int(son1) / int(son2)}")
            else:
                print('Faqat raqam kiriting!')
        else:
            print('Faqat raqam kiriting!')