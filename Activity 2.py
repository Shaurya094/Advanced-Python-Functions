x = {1, 3, 5}
y = {2, 4}
z = list(zip(x,y))
print(z, "\n")
print ("\n")

c = [10, 20, 30 , 40]
v = [400, 300, 200, 100]
print ("List 1: ", c, "\nList 2: ", v)
for x,y in zip (c, v[::-1]):
    print (x,y)
print ("\n \n")

stocks = ['infosys', 'nike', 'apple']
prices = [12334, 3934, 7783]

dict = {stocks: prices for stocks,
                    prices in zip(stocks, prices)}
print ('\n{}'.format (dict))