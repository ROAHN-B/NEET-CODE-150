prices = [7,1,5,3,6,4]
max_prof=0
min_price=prices[0]

for ele in prices:
    if ele <min_price:
        min_price=ele
    elif ele-min_price>max_prof:
        max_prof=ele-min_price
print (max_prof)
    
        

