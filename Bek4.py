# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 01:31:17 2022

@author: USER
"""

moshinalar=["lasetti","tiko","nexia","damas","kaptiva","gm","maluba"]
for avto in moshinalar:
    print(avto.title())
for avto in moshinalar:
    if avto == "gm":
        print(avto.upper())
    else:
        print(avto.capitalize())
for avto in moshinalar:
    if avto != "gm":
        print(avto.lower())
    else:
        print(avto.upper())
ism=input("Ismingizni kiriting?\n>>>")
if ism != "Jasurbek":
        print(f" Assalomu aleykum { ism.upper() }. Foydalanuvchilar ro`yhatini ko`rishingiz mumkin")
else:
        print("Xush kelibsiz", ism)
son=input("son kiriting?\n>>>")
son2=input("ikkinchi sonni kiriting?\n>>>")
if son == son2:
    print("Bu sonlar teng")
else:
    print("Bu sonlar teng emas")
son=int(input("Sonni kiriting?\n>>>"))
if son>0:
    print("Musbat son")
else:
    print("Manfiy son")
son=float(input("Son kiriting?>>>"))
if son>0:
    print(son**(1/2))
else:
    print("Musbat son kiriting")