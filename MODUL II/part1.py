#
#
# #int
# number  = int('3')
#
# print("Nr as text", type(number))
# print("Address is:", id(number))
#
# number1  = 3
#
# print("Nr as text", type(number1))
# print("Address is:", id(number1))
#
# print("check if equal :",number1 == number)
#
# #float
# number2 = 3.1
#
# print(type(number2))
# print("Address is:", id(number2))
#
#
#
#
# #bool
# bool_object = False
# print(type(bool_object))
# print("Address is:", id(bool_object))
#
# print("convert to bool: ", bool(1))
# print("convert to int: ", int(True))
#
#
# print(5//3)


# 1.
# A=1/2*b*h
#
# b= int(input("b:"))
# h= int(input("h:"))
#
# print("Aria este",1/2*b*h)
#


# 2.
#
# password = "7710"
#
# parola = input("parola calculatorului este:")
#
# print("check if correct :", parola == password)
#

# parola=int(input('Introduceti parola:'))
# parola_salvata=7710
# if parola==parola_salvata:
#     print('True')
# else:
#     print('False')


# 3.

# a= int(input("a:"))
# b= int(input("b:"))
#
# # print("Media celor 2 numere este:",(a+b)/2)
# # print("Impartirea numerelor:",a/b)
# # print("Impartirea numerelor:",a**b)
#
# print("Media celor 2 numere este:",(a+b)/2,"\nImpartirea numerelor:",a/b,"\nImpartirea numerelor:",a**b)
#
#
# media = (a+b)/2
# impartire = a/b
# putere = a**b
#
# print(media)

# 4.





venitluna= int(input("venit pe luna:"))


print("Recomandarile noastre:")
print("Cheltuieli uzuale:",50/100*venitluna)
print("Recreere:",30/100*venitluna)
print("Economii si datorii:",20/100*venitluna)



a = 50/100*venitluna
b = 30/100*venitluna
c = 20/100*venitluna


print("Recomandarile noastre:","\nCheltuieli uzuale:",a,"\nRecreere:",b,"\nEconomii si datorii:",c)




a = 3
b = 4
c = 5

x = (-b+((b**2-4*a*c)**(1/2)))/(2*a)

print(x)


a=3
b=4
c=5

print('rezultatul este:', (-b+((b**2-4*a*c)**(1/2)))/(2*a))