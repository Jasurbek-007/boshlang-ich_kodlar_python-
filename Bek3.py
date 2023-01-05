# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 00:30:57 2022

@author: USER
"""
sonlar=list(range(1,10))
for son in sonlar:
    print(f"2 * {son} = {son*2}")
dostlar=["Chori","Panji","Suxrop","Alish","Normat","Azim"]
for dost in dostlar:
    print("Salom",dost)
    print("Hayr",dost)
print("Bu mening do`stlarim")    
takror=len(dostlar)
print(f"Bu yerda kod {takror} marta takrorlandi ")
toq_sonlar=list(range(9,100,2))
print(toq_sonlar)
for son in range(9,100,2):
    print(f"{son} ** {3} = {son**3}")
    print(son**3)
kinolar=[]
print("5 ta eng yaqin do`stingizning ismini kiriting?")
for kino in range(5):
    kinolar.append(input(f"{kino+1} Do`stingizning ismini kiriting?\n>>>"))
print(kinolar)
uchrashgan_odamlar=[]
print("Bugun uchrashgan odamlarizni ismlarini ayting?")
for odam in range(0,6):
    uchrashgan_odamlar.append(input(f"{odam+1} Suxbatlashgan odamlarizni ismini kiriting?\n>>>" ))
print(uchrashgan_odamlar)