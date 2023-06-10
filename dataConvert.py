from parsefile import data_list

result = {}

for item in data_list:
    # Извлекаем основную часть имени, удаляя числа
    name_base = ''.join(filter(str.isalpha, item['name']))

    if name_base not in result:
        result[name_base] = {'volume': 0, 'price': 0, 'name': name_base}

    result[name_base]['volume'] += item['volume']
    result[name_base]['price'] += item['price']

# Преобразуем результат обратно в список словарей
clear_data = list(result.values())