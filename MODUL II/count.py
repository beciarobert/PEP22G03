# from collections import Counter
# method 1

# cuvinte = [ "cuvant1","cuvant2","cuvant3","cuvant1","cuvant3","cuvant6","cuvant7",]
#
# print("cuvant1 : ",cuvinte.count("cuvant1"))
# print("cuvant2 : ",cuvinte.count("cuvant2"))
# print("cuvant3 : ",cuvinte.count("cuvant3"))
# print("cuvant4 : ",cuvinte.count("cuvant4"))
# print("cuvant5 : ",cuvinte.count("cuvant5"))
# print("cuvant6 : ",cuvinte.count("cuvant6"))
# print("cuvant7 : ",cuvinte.count("cuvant7"))

# method 2

# cuvinte = [ "cuvant1","cuvant2","cuvant3","cuvant1","cuvant3","cuvant6","cuvant7",]
#
# print(Counter(cuvinte))

# method 3

# wordList = ["word1", "word2", "word3", "word4", "word5"]
# reviews = ["word1 word1 word2 word2", "word1 word3 word2 word6" ]
# # step 1 and 2
# summaryDict = {}
# for review in reviews:
#     for word in review.split():
#         if word in summaryDict:
#             summaryDict[word] += 1
#         else:
#             summaryDict[word] = 1
# # step3
# filteredDict = {k: v for k, v in summaryDict.items() if k in wordList}
#
# print(filteredDict)
#
#
# print("please wait...")
# time.sleep(1)
# print("5")
# time.sleep(1)
# print("4")
# time.sleep(1)
# print("3")
# time.sleep(1)
# print("2")
# time.sleep(1)
# print("1")
# time.sleep(0.5)
# print("DONE")


# print("loading...")
# time.sleep(1)
# print("3")
# time.sleep(1)
# print("2")
# time.sleep(1)
# print("1")
# webbrowser.open("https://www.youtube.com/watch?v=Ylwd5ugJ2hQ")
#

import time
import webbrowser
import datetime
import AppKit
import beepy
import simpleaudio
import Cocoa
import os


rn = str(datetime.datetime.now().time())
print(rn)

# loop = True
#
# while loop:
#     rn = str(datetime.datetime.now().time())
#     print(rn)
#     if rn >= "00:39:00":


Cocoa.NSBeep()
