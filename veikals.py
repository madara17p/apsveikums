saraksts = ["Elchin", "cepums", "7.klase","Madara", "Amelija", "Evelina"]
#               0         1         3

print(saraksts[0])

while True:

# skaitlis = int(input("Ievadi produkta indeksu:")) 
# print(saraksts[skaitlis])
    darbiba = input("Ievadi dzēst vai jauns:")

    if darbiba == "dzest nosaukumu":
        produkts_kas_jaizdzes = input("'Ievadi indeksu, kuru gribi izdzēst:")
        saraksts.remove(produkts_kas_jaizdzes)
        print(saraksts)

    elif darbiba == "dzest":
        produkts_kas_jaizdzes = int(input("Ievadi indeksu, kuru gribi izdzēst:"))
        saraksts.pop(produkts_kas_jaizdzes)
        print(saraksts)
  
    elif darbiba == "jauns":
        jauns_produkts = input("Ievadi produkta indeksu:")
        saraksts.append(jauns_produkts)
        print(saraksts)
        
    else:
        break   