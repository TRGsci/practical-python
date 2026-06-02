symbols = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
symlist = symbols.split(',')
symlist.append('RHT')
symlist.insert(1, 'AA')
symlist.remove('MSFT')
symlist.append('YHOO')
x = ','.join(symlist)
print(symlist)
print(x)
