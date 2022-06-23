

# def verify():
#     good_pass = False
#     while not good_pass:
#         parola = input("Introduceti o parola: ")
#         if len(parola) < 8:
#             print("Parola trebuie sa aiba lungimea mai mare de 7 caractere")
#         for number in range(0,10):
#             if str(number) in parola:
#                 break
#         else:
#             print("Parola trebuie sa contina o cifra")
#             continue
#         for letter in "@!%":
#             if letter in parola:
#                 break
#         else:
#             print("Parola trebuie sa contina una din urmatoarele caractere: @, !, %")
#         if parola[0] == parola[0].upper():
#             good_pass = True
#         else:
#             print("Parola trebuie sa inceapa cu litera mare")
#
#
# verify()



#
# def power():
#     numar = int(input("introdu un numar:"))
#     while True:
#         print(numar ** 2)
#         if input("Q for exit /").lower() == "q":
#             break
#         else:
#             continue
# power()

######################################################################
#
# def office():
#     credentials = {}
#     for i in range(1,4):
#         PCs_user = input(f"Introduceti utilizatorul PC-ului {i}: ")
#         PCs_pasw = input(f"Introduceti parola PC-ului {i}: ")
#         credentials[PCs_user] = PCs_pasw
#     for key in credentials:
#         print(f"{key} -> {credentials[key]}")
#
# office()



######################################################################