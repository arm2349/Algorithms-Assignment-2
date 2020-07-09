def change_money(m):
    assert m>=1 and m<=1000
    amount_given=m
    coins=[10,5,1]
    minimum_coins=0
    for i in range(len(coins)):
        while amount_given>=coins[i]:
            minimum_coins+=1
            amount_given-=coins[i]
    return minimum_coins
inp=int(input())
print (change_money(inp))
