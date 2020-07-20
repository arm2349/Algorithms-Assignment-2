def change_money(m, coins=(10,5,1), print_change=False):
    assert 1<= m<=1000
    amount_given=m
    num_coins=[0 for i in range(len(coins))]
    for i in range(len(coins)):
        if amount_given==0:
            break
        coin=coins[i]
        quotient_and_remainder=divmod(amount_given, coin)
        num_coins[i]=quotient_and_remainder[0]
        amount_given=quotient_and_remainder[1]
    return sum(num_coins)
