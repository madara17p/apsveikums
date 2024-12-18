# izveidot tukšu sarakstu
#izveidot ciklu kas visu laiku ptsa lietotājam
# pievienot jaunu elementu
# un izpratnē sarakstu
# kad lietotājs ievada STOP, programma beiz darbu

saraksts = []

while True:
    vards = input("Ievadi vārdu:")
    if vards == "stop":
        break
    saraksts.append(vards)
    print(saraksts)


import random
skaitlis = random.randint(1, 10)
print(skaitlis)