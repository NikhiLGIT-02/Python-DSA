def max_profit(prices):
    min_price=float('inf')
    max_profit=0

    for price in prices:
        if price<min_price:
            min_price=price
        profit=price-min_price    

        if profit>max_profit:
            max_profit=profit
        
    return max_profit


#Main
nums=[7,1,5,3,6,4]
print(float('inf'))
print(max_profit(nums))