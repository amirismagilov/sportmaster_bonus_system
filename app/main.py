from datetime import date
from lib import *

data_now = date.today()
date_of_deleting_bonus = date(2019, 3, 11)
min_date_of_transferring_bonus = date(2019, 1, 1)
max_date_of_transferring_bonus = date(2019, 3, 10)

total_bonus = 0
total_bonus_for_transfer = 0


gift_card_sum = 0
amount = 0

gift_card = 0 #принимает значение 0 - если покупается не подарочная карта, 1 - если подарочная карта
best_price = 0 #принимает значение 0 - если товар не по акции "Лучшая цена", 1 - если по акции
discount_shop = 0 #принимает значение 0 - если магазин СПОРТМАСТЕР-ДИСКОНТ, 1 - если нет
discount = 0 #принимает значение 0 - если товар без скидки, 1 - если по скидке

if conditions_check(gift_card, best_price, discount_shop, discount) == True:
    bonus_per_purchase_calculation(amount, gift_card_sum, coefficent)

    if date_of_deleting_bonus.day == data_now.day and date_of_deleting_bonus.month == data_now.month: #проверка даты анунулирования бонусов
        bonus_total = total_bonus_for_transfer

    if min_date_of_transferring_bonus <= data_now <= max_date_of_transferring_bonus: #проверка периода переноса бонусов на следующий год
        total_bonus_for_transfer = bonus_per_purchase_calculation(amount, gift_card_sum,coefficent_calculation(total_bonus))


    print(bonus_total)

