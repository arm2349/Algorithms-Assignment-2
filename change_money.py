def change_money(m):
    assert 1<= m<=1000
    amount_given=m
    coins=[10,5,1]
    minimum_coins=0
    for i in range(len(coins)):
        if amount_given==0:
            break
        coin=coins[i]
        quotient_and_remainder=divmod(amount_given, coin)
        minimum_coins+=quotient_and_remainder[0]
        amount_given=quotient_and_remainder[1]
    return minimum_coins
