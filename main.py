money = int(input("Введите сумму:"))
print(money)

per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
bank_deposit = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

accumulation_TKB = money / 100 * per_cent['ТКБ']
accumulation_SKB = money / 100 * per_cent['СКБ']
accumulation_VTB = money / 100 * per_cent['ВТБ']
accumulation_SBER = money / 100 * per_cent['СБЕР']

deposit.append(int(accumulation_TKB))
deposit.append(int(accumulation_SKB))
deposit.append(int(accumulation_VTB))
deposit.append(int(accumulation_SBER))

bank_deposit['ТКБ'] = accumulation_TKB
bank_deposit['СКБ'] = accumulation_SKB
bank_deposit['ВТБ'] = accumulation_VTB
bank_deposit['СБЕР'] = accumulation_SBER

max_bank_deposit = max(bank_deposit, key=bank_deposit.get)

print(deposit)
#print (max(bank_deposit, key=bank_deposit.get))
print('Максимальная сумма, которую вы можете заработать —', str(max(deposit)),)
print('В банке -', str(max_bank_deposit),)