from forex_python.converter import CurrencyRates

c = CurrencyRates()
dolarkuru = c.get_rates('USD')
eurokuru = c.get_rates('EUR')
print("Anlık dolar kuru : ",dolarkuru)
print("Anlık euro kuru : ",eurokuru)
with open ("dolar.txt","a") as myfile:
    myfile.write("Dolar kuru : "+str(dolarkuru))
    myfile.write("\n")
with open ("euro.txt","a") as myfile:
    myfile.write("Euro kuru : "+str(eurokuru))
    myfile.write("\n")