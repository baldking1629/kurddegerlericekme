from forex_python.converter import CurrencyRates

c = CurrencyRates()
dolarkuru = c.get_rate('USD','TRY')
eurokuru = c.get_rate('EUR','TRY')
print("Anlık dolar kuru : ",dolarkuru)
print("Anlık euro kuru : ",eurokuru)
dolarkuru = round(dolarkuru,4)
with open ("kurdegerleri.txt","a") as myfile:
    myfile.write("Dolar kuru : "+str(dolarkuru))
    myfile.write("\n")
    myfile.write("Euro kuru : "+str(eurokuru))
    myfile.write("\n")