def bonus_per_purchase_calculation(amount, gift_card_sum,coefficent):
    """
    >>> bonus_per_purchase_calculation(5400, 0,100)
    500
    """
    bonus_per_purchase = (amount - gift_card_sum) // 1000 * coefficent
    return bonus_per_purchase

def coefficent_calculation(total_bonus):
    """
    >>> coefficent_calculation(7_000)
    50
    >>> coefficent_calculation(16000)
    70
    >>> coefficent_calculation(160000)
    100
    """
    if total_bonus <= 15_000:
        coefficent = 50
    elif  15_000 < total_bonus <= 150_000:
        coefficent = 70
    elif total_bonus > 150_000:
        coefficent = 100
    return coefficent

def conditions_check(gift_card, best_price, discount_shop, discount):
    """
    >>> conditions_check(0,0,0,0)
    True
    >>> conditions_check(1,0,0,0)
    False
    >>> conditions_check(0,1,0,0)
    False
    >>> conditions_check(0,0,1,0)
    False
    >>> conditions_check(0,0,0,1)
    False
    """
    if gift_card == 1 or best_price == 1 or discount_shop == 1 or discount == 1:
        return False
    else:
        return True

