names = ["Anna", "Oskars", "Markuss"]

#for name in names:
#    print(f" Hey hey {name}!")



ages = [16, 15, 16]
university = [False, False, True]
personal_data =[
            ["Anna", 16, False, "anna@somemail.com"], 
            ["Oskars", 15, False, "oskars.poskars@besstmail.com"], 
            ["Markuss", 16, True, "markusiks@ggmail.com"] 
]

personal_data.append(["Inga", 20, False, "inga@gmail.com"])

name = input('Enter your name: ')
age = int(input('Enter your age: '))
university = input('Are you in university? (yes/no): ').lower() == 'yes'
email = input('Enter your email: ')

new_data = [name, age, university, email]
personal_data.append(new_data)

for rinda in personal_data:
        print(f"Aizsūtam e-pastu uz adrese {rinda[3]}")

