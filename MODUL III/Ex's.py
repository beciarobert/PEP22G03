# Ex 1
#
# secret_number = 777
#
# print(
#     """
#     +================================+
#     | Welcome to my game, muggle!    |
#     | Enter an integer number        |
#     | and guess what number I've     |
#     | picked for you.                |
#     | So, what is the secret number? |
#     +================================+
#     """)
#
# sn = int(input("Input here:"))
#
# if sn != secret_number:
#     print("Ha ha! You're stuck in my loop!")
# while sn != secret_number:
#     sn = int(input("Try again!:"))
#
# print("Well done, muggle! You are free now.")


# Ex 2

# import time
#
# for i in range(1,6):
#     print(f"{i} Mississippi")
#     time.sleep(1)


# Ex 3

# keyword = "chupacabra"
# while True:
#     word = input("Enter a word:")
#     if word == keyword:
#         break
#
#
# print("You've left the loop")

# Ex 4

# word = input("Input a word:").upper()
#
#
# for letter in word:
#     if letter in "AEIOU":
#         continue
#     print(letter)

# Ex 5

# word = input("Input a word:").upper()
#
# true_word = ""
# for letter in word:
#     if letter in "AEIOU":
#         continue
#     true_word += letter
#
# print(true_word)

# Ex 6

# blocks = int(input("Number of blocks: "))
# layers = 1
# height = 0
# while layers <= blocks:
#     height += 1
#     blocks -= layers
#     layers += 1
#     print(layers)
# print("The height of the pyramid:", height)
# print(height)

# Ex 7

c0 = int(input("Input here:"))
steps = 0

while c0 >= 1 and c0 != 1:
    if c0 % 2 == 0:
        c0 = c0 // 2
        steps += 1
    else:
        c0 = 3 * c0 + 1
        steps += 1

    print(c0)
    if c0 != 1:
        continue

print(f"The number of steps: {steps}")