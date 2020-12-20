import requests, json

coin = str.upper(input("Select Your Coin:"))
CGPriceRaw = requests.get("https://api.coingecko.com/api/v3/simple/price?ids="+coin+"&vs_currencies=usd")
BNCPriceRaw = requests.get("https://api3.binance.com/api/v3/ticker/price?symbol="+btc+"USDT")
BNCDict = BNCPriceRaw.json()
CGDict = CGPriceRaw.json()
BNCPrice = float(BNCDict.get('price'))
CGGross = dict(CGDict.get('dai'))
CGPrice = float(CGGross.get('usd'))
Agg = str((CGPrice + BNCPrice)/2)
print(coin)
print()
print("The current Coingecko price is: $" + str(CGPrice))
print("The current Binance price is: $" + str(BNCPrice))
print()
print("Making the current aggregate $ " + Agg)




