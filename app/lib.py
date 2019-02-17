def bonus_per_purchase_calculation(amount, gift_card_sum, coefficent):  # сколько бонусов начисляется при одной покупки
    """
    >>> bonus_per_purchase_calculation(5400, 0,100)
    500
    """
    bonus_per_purchase = (amount - gift_card_sum) // 1000 * coefficent
    return bonus_per_purchase


def coefficent_calculation(sum_of_purchase):
    """
    >>> coefficent_calculation(7_000)
    50
    >>> coefficent_calculation(16_000)
    70
    >>> coefficent_calculation(160000)
    100
    """
    if sum_of_purchase <= 15_000:
        coefficent = 50
    elif 15_000 < sum_of_purchase <= 150_000:
        coefficent = 70
    elif sum_of_purchase > 150_000:
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


def bonus_to_written_off__calculation(amount, total_bonus):
    """
    >>> bonus_to_written_off__calculation(5_000, 1_500)
    1500
    >>> bonus_to_written_off__calculation(3_000, 500)
    500
    >>> bonus_to_written_off__calculation(1_001, 5_000) #doctest + ELLIPSIS
    300.3
    """
    possible_procent_written_off = 0.3
    possible_amount_written_off = float(amount * possible_procent_written_off)
    if possible_amount_written_off >= total_bonus:
        bonus_to_written_off = total_bonus
    else:
        bonus_to_written_off = possible_amount_written_off
    return bonus_to_written_off
