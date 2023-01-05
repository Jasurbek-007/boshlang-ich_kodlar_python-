# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 23:16:11 2022

@author: USER
"""

kocha="Bog`bon"
mahalla="Sag`bon"
tuman="belka"
viloyat="Samarqand"
print(viloyat.upper()+" viloyati, "+tuman.title()+" tumani, "+mahalla.lower()+
" \nmahallasi, "+kocha.capitalize()+" ko`chasida yashayman. ")
viloyat=input("Qaysi viloyatda tug`ilgansiz?\n>>>")
uman=input("Qaysi tumanda tug`ilgansiz?\n>>>")
mahalla=input("Qaysi mahallada tug`ilgansiz?\n>>>")
kocha=input("Qaysi ko`chada tug`ilgansiz?\>>>")
print(viloyat.upper()+" viloyati")
print(tuman.title()+" tumani")
print(mahalla.lower()+" mahallasi")
print(kocha.capitalize()+" ko`chasida tug`ilganman")
yangi_manzil=f"{viloyat} viloyati {tuman} tumani {mahalla} \nmahallasi {kocha} ko`chasi yashayman"
print(yangi_manzil.upper())
son=int(input("son kiriting\n>>>"))
print(son,"ning kvadrati",son**2, "ga teng")
print(son,"ning kubi",son**3,"ga teng")
yosh=input("Yoshingizni kiriting\n>>>")
t_yil=2022-int(yosh)
print("Siz ",t_yil, " chi yilda tug`ilgansiz")
son=int(input("Birinchi sonni kiriting\n>>>"))
son1=int(input("Ikkinchi sonni kiriting\n>>>"))
yigindi=son+son1
ayirma=son-son1
kopaytma=son*son1
bolinma=son//son1
bolinma1=son/son1
son2=f"{son} + {son1} = {yigindi}"
son3=f"{son} - {son1} = {ayirma}"
son4=f"{son} * {son1} = {kopaytma}"
son5=f"{son} // {son1} = {bolinma}"
son6=f"{son} / {son1} = {bolinma1}"
print(son2)
print(son3)
print(son4)
print(son5)
print(son6)