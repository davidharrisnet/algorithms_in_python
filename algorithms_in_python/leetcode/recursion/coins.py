

def coin_machine(coins, days):
    if days == 1:
        return coins
    else:
        #coin_count = coin_machine(coins * 2, days -1)
        coin_count = coin_machine(coins, days -1) * 2
     
    return coin_count   


total_coins = coin_machine(2,5)
print(total_coins)