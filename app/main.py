from datetime import date
from lib import *

#параметры даты:
data_now = date.today()
date_of_deleting_bonus = date(2019, 3, 11)
min_date_of_transferring_bonus = date(2019, 1, 1)
max_date_of_transferring_bonus = date(2019, 3, 10)

#параметры бонусов:
total_bonus = 100
total_bonus_for_transfer = 0

#параметры покупок:
gift_card_sum = 0
amount = 10_000
sum_of_purchase = 15_0000


gift_card = 0
best_price = 0
discount_shop = 0
discount = 0


sum_of_purchase += amount
coefficent = coefficent_calculation(sum_of_purchase)



if date_of_deleting_bonus.day == data_now.day and date_of_deleting_bonus.month == data_now.month: #проверка даты анунулирования бонусов
    bonus_total = 0

elif min_date_of_transferring_bonus <= data_now <= max_date_of_transferring_bonus: #проверка периода переноса бонусов на следующий год
    total_bonus_for_transfer += bonus_per_purchase_calculation(amount, gift_card_sum, coefficent)
    total_bonus = total_bonus_for_transfer
    # print("Количество бонусов: ", total_bonus_for_transfer)

else:
    total_bonus += bonus_per_purchase_calculation(amount, gift_card_sum, coefficent) + total_bonus_for_transfer
print("Количество бонусов: ", total_bonus)

if conditions_check(gift_card, best_price, discount_shop, discount) == True:
    bonus_to_written_off = bonus_to_written_off__calculation(amount, total_bonus)
print("Количество бонусов, доступных для списания: ", bonus_to_written_off)