from forex_python.converter import CurrencyRates

c = CurrencyRates()
dolarkuru = c.get_rate('USD','TRY')
eurokuru = c.get_rates('TRY')
print("Anlık dolar kuru : ",dolarkuru)
print("Anlık euro kuru : ",eurokuru)