from dataConvert import clear_data

total_price = 0
total_volume = 0

for user in clear_data:
    total_price += user['price']
    total_volume += user['volume']

for user in clear_data:
    user['total-price'] = total_price
    user['total_volume'] = total_volume
    user['price-percent'] = round(user['price']/total_price, 2)
    user['volume-percent'] = round(user['volume']/total_volume, 2)
    user['payment'] = round(3.25 * user['volume-percent'], 4)
    print(f'{user["name"]} накопал {user["volume-percent"]*100}% и должен заплатить {user["payment"]}')