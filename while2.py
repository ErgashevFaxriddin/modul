# _______________________________________________________________________________________

# g = [1, 2, 3, 4, 5, 6 , 7, 8, 9]

# print(
#         """f
       
#       {g[0]} | {g[0]} | {g[0]}
#       ----------
#       {g[0]} | {g[0]} | {g[0]}
#       ----------
#       {g[0]} | {g[0]} | {g[0]}
      
# """
#       )

# while True:
#     x = int(input('X= '))
#     g[x -1] = 'X'
    
#     print(
#         """f
       
#       {g[0]} | {g[0]} | {g[0]}
#       ----------
#       {g[0]} | {g[0]} | {g[0]}
#       ----------
#       {g[0]} | {g[0]} | {g[0]}
      
# """
#       )
#     if g[0]==g[1] and g[1]== g[2] or g[4]==g[5] and g[5]== g[6] or g[7]==g[8] and g[8]== g[9] or g[1]==g[4] and g[5]==g[7] or g[2]==g[5] and g[5]==g[8] or g[3]==g[7] and g[7]==g[9] or g[1]==g[5] and g[5]==g[9] or g[3]==g[5] and g[5]==g[7]:
#         print('X yutdi. Tamom')
#         break
    
#     print(
#         """f
       
#       {g[0]} | {g[0]} | {g[0]}
#       ----------
#       {g[0]} | {g[0]} | {g[0]}
#       ----------
#       {g[0]} | {g[0]} | {g[0]}
      
# """
#     )

#     o = int(input('0 ni kiriting: '))
#     g[o -1] = 'O'
#     if g[0]==g[1] and g[2]== g[3] or g[4]==g[5] and g[5]== g[6] or g[7]==g[8] and g[8]== g[9] or g[1]==g[4] and g[5]==g[7] or g[2]==g[5] and g[5]==g[8] or g[3]==g[7] and g[7]==g[9] or g[1]==g[5] and g[5]==g[9] or g[3]==g[5] and g[5]==g[7]:
#         print('X yutdi. Tamom')
#         break
    
# ____________________________________________________________________________________________________

g = [' ' for _ in range(9)]  
while True:
    x = int(input("X ni kiriting (1-9): ")) - 1
    if g[x] != ' ':
        print("Bu joy band! Qayta urinib ko'ring.")
        continue
    g[x] = 'X'

    print(f"""
      {g[0]} | {g[1]} | {g[2]}
      ----------
      {g[3]} | {g[4]} | {g[5]}
      ----------
      {g[6]} | {g[7]} | {g[8]}
    """)

    if (g[0] == g[1] == g[2] != ' ') or (g[3] == g[4] == g[5] != ' ') or (g[6] == g[7] == g[8] != ' ') or \
       (g[0] == g[3] == g[6] != ' ') or (g[1] == g[4] == g[7] != ' ') or (g[2] == g[5] == g[8] != ' ') or \
       (g[0] == g[4] == g[8] != ' ') or (g[2] == g[4] == g[6] != ' '):
        print("X yutdi. Tamom")
        break

    o = int(input("O ni kiriting (1-9): ")) - 1
    if g[o] != ' ':
        print("Bu joy band! Qayta urinib ko'ring.")
        continue
    g[o] = 'O'

    print(f"""
      {g[0]} | {g[1]} | {g[2]}
      ----------
      {g[3]} | {g[4]} | {g[5]}
      ----------
      {g[6]} | {g[7]} | {g[8]}
    """)

    if (g[0] == g[1] == g[2] != ' ') or (g[3] == g[4] == g[5] != ' ') or (g[6] == g[7] == g[8] != ' ') or \
       (g[0] == g[3] == g[6] != ' ') or (g[1] == g[4] == g[7] != ' ') or (g[2] == g[5] == g[8] != ' ') or \
       (g[0] == g[4] == g[8] != ' ') or (g[2] == g[4] == g[6] != ' '):
        print("O yutdi. Tamom")
        break

    if ' ' not in g:
        print("Durrang! O'yin tugadi.")
        break