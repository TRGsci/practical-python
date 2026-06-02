stockticker = 'HPQ,AAPL,IBM,MSFT,YHOO,DOA,GOOG'
stklist = stockticker.split(',')
stklist.append('RHT')
stklist.insert(1, 'AA')
stklist.remove('MSFT')
stklist.append('YHOO')
x = ','.join(stklist)
print(stklist)
print(x)
