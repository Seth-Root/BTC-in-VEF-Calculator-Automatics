# -*- coding: utf-8 -*-
# -*- encoding: utf-8 -*-


import urllib2
from bs4 import BeautifulSoup
import re

Value_Euro_in_bolivar = 0
Value_Euro_in_bolivar = 0
value_BTC_dolares = 0


url = "http://www.eleconomista.es/cruce/BTCUSD"

page = urllib2.urlopen(url)

soup = BeautifulSoup(page, "lxml")
valor_btc = soup.find_all('span',class_="accion1 Dif_23138 estado_23138" )



for valores in valor_btc:
               
                               value_BTC_dolares = valores.get_text()
                               value_BTC_dolares = float(value_BTC_dolares.replace(',','.'))
   
url = "https://twitter.com/dolartoday?lang=es"

page = urllib2.urlopen(url)

soup = BeautifulSoup(page, "lxml")
valores_dolar_euro = soup.find_all('p',class_="ProfileHeaderCard-bio u-dir" )



for valores in valores_dolar_euro:
               
                               valor_dolar_euro = valores.get_text()
                               valor_dolar_euro = valor_dolar_euro.replace(',','.')
                               value_Dolar_in_bolivar = re.findall('(\d+.[0-9]+?) y el', valor_dolar_euro)
                               value_Dolar_in_bolivar = float(value_Dolar_in_bolivar[0])
                               print "1 Dolar Vale", value_Dolar_in_bolivar, "Bolivares"

                               Value_Euro = re.findall('(\d+.[0-9]+?) entra', valor_dolar_euro)
                               Value_Euro = float(Value_Euro[0])
                               print "1 Euro Vale", Value_Euro, "Bolivares"

                                
                





BTC_in_satoshi = 100000000

#amount_satoshis = int(input("write Amount Satoshis:") )

amount_satoshis = int(input("Escribe La cantidad de Satoshis:") )

BTC_in_Euros = value_BTC_dolares * (Value_Euro/value_Dolar_in_bolivar)

print "Value BTC", value_BTC_dolares, " Dolars"
print "Value BTC", BTC_in_Euros, " Euros"


calc_Euros = ((amount_satoshis * BTC_in_Euros )*1.00000 / BTC_in_satoshi)

print "Value ",amount_satoshis ,"Satoschis, it's ", calc_Euros, " Euros"

calc_dolares = (amount_satoshis * value_BTC_dolares)*1.00000 / BTC_in_satoshi

print "Value  ",amount_satoshis ,"Satoschis, it's ", calc_dolares, "Dolares"