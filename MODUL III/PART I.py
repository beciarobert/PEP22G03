# my_age = -1
#
#
# if my_age > 18:
#     print("you are an adult")
# elif my_age > 13:
#     print("you are a teenager")
# elif my_age >= 0:
#     print("you are a child")
# else:
#     print("negative age")



#
# a = ""
# b = "a"
#
# if a:
#     print(b)
# else:
#     print(a)
#
# print(a and b)
#
#
# if a:
#     print(a)
# else:
#     print(b)
#
#
# print(a or b)
#


################################################################################################
#               EX 1
# Introduceti primele 7 cifre din CNP :
# Aveti peste 18 ani
#
#

# 1970707
# 0123456

# 1 = baiat
# 2 = fata
#
# 5 = baiat
# 6 = fata

# CNP = input("Introduceti primele 7 cifre din CNP: ")
#
# an_nastere = int(CNP[1:3])
# an_curent = 2022
#
# if int(CNP[0]) <=2:
#     an_nastere+=1900
#
# else:
#     an_nastere+=2000
#
# varsta = an_curent - an_nastere
#
# if varsta > 18:
#     print("Aveti peste 18 ani")
# else:
#     print("Nu aveti peste 18 ani")
#
#
# print(varsta)

################################################################################################
#                              EX 2


# Take input from user a number and count from 0 to the inserted number printing all even numbers

# number = int(input("Type a number: "))
# start = 0
#
# while True:
#     if start+2 <= number:
#         start+=2
#         print(start)
#     else:
#         break

# if start+2 <= number:
#     start+=2
#     print(start)
# if start+2 <= number:
#     start+=2
#     print(start)
# if start+2 <= number:
#     start+=2
#     print(start)



# count = 1
#
# while count <= 4:
#     count += 1
#     if count == 4:
#         break
#     print("run")


# numar = int(input("Introduceti un numar: "))
# i = 0
# while i <= numar:
#     if i % 2 == 0:
#         print(i)
#     i += 1


################################################################################################
#                              EX 3
#Coffe machine has these options : Cappuccino, Espresso
#Cappuccino = 4 lei ; Espresso = 3.5 lei
#Coffe machine accepts only 5 lei and 10 lei

#Show menu, ask for coffee ; If user asked for a valid option ; coffe machine asks for money ; If valid money return change and coffee


#
#
# print("1. Cappuccino     ... 4 lei","2. Espresso       ... 3.5 lei",sep="\n")
#
# Cappucino = 4
# Espresso = 3.5
# optiune = False
#
#
# while not optiune:
#     optiune = int(input("Ce optiune alegeti? [1,2]: "))
#     if optiune == 1:
#         print("Ati ales optiunea 1")
#     elif optiune == 2:
#         print("Ati ales optiunea 2")
#     else:
#         print("Alegere gresita")
#         optiune = False
#
#
#
# while True:
#     bani = int(input("Introduceti o banconta [5,10]: "))
#     if bani == 5:
#         print("Ati introdus 5 lei")
#         break
#     elif bani == 10:
#         print("Ati introdus 10 lei")
#         break
#     else:
#         print("Se permit doar bancnote de 5 sau 10 lei")
#
#
#
# if optiune == 1:
#     print(f"Veti primi restul de {bani-Cappucino} lei","Produsul se livreaza...",sep="\n")
# elif optiune == 2:
#     print(f"Veti primi restul de {bani- Espresso} lei", "Produsul se livreaza...", sep="\n")
#

################################################################################################

#                           EX 4
#
# parola = 7788
#
# while True:
#     passw = int(input("Parola este : " ))
#     if passw == parola:
#         print("Acces permis")
#         break
#     else:
#         print("Parola gresita. Mai incercati")
#

#////////////////////////////////////////////////////////////
# count = 0
#
# while input("Introduceti parola:") != "7788":
#     print("Parola gresita")
#     count += 1
#     if count == 3:
#         print("Ati gresit de 3 ori. Acces respins")
#         break
# else:
#     print("Acces permis")
#




################################################################################################



#                              EX 3
#Coffe machine has these options : Cappuccino, Espresso
#Cappuccino = 4 lei ; Espresso = 3.5 lei
#Coffe machine accepts only 5 lei and 10 lei

#Show menu, ask for coffee ; If user asked for a valid option ; coffe machine asks for money ; If valid money return change and coffee


# Meniu :
# Cappucino ... 4 lei
# Espresso  ... 3.5 lei

# Alege optiunea[1,2] :
# Introdu bancnota[5,10] :

# Veti primi restul de ...

# Cappucino = 4
# Espresso = 3.5
#
#
# print("Meniu:")
# print("1.Cappucino ... 4 lei")
# print("2.Espresso  ... 3.5 lei")
#
# while True:
#     optiune = int(input("Alege optiunea[1,2]:"))
#     if optiune == 1:
#         print("Ai ales optiunea 1")
#         break
#     elif optiune == 2:
#         print("Ai ales optiunea 2")
#         break
#     else:
#         print("Ati gresit")
#
# while True:
#     bani = int(input("Introdu bancnota[5,10]:"))
#     if bani == 5:
#         print("Ati introdus 5 lei")
#         break
#     elif bani == 10:
#         print("Ati introdus 10 lei")
#         break
#     else:
#         print("Se permit doar bancnote de 5 si 10 lei")
#
#
#
# if optiune == 1:
#     print(f"Veti primi restul de {bani - 4}")
# elif optiune == 2:
#     print(f"Veti primi restul de {bani - 3.5}")