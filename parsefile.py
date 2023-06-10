import re
import glob


def parse_line(data):
    data_clean = re.sub(r'<localized hint="[^"]*">|</localized>', '', data)
    data_clean = data_clean.replace('*', '')
    elements = data_clean.split('\t')
    return elements


def parse_file(filename):
    # Загружаем данные из файла
    with open(f'{filename}', 'r', encoding='utf-8') as f:
        raw_data = f.read()

    # Допустим, что каждый новый массив данных начинается с новой строки
    data_arrays = raw_data.split('\n')

    # Теперь мы можем применить функцию `parse` к каждому из массивов
    parsed_data = [parse_line(data) for data in data_arrays]

    # Убираем строчку с названиями данных, типа "звёздная система, дата, время"
    parsed_data.pop(0)

    username = re.search(r'/([^/]*).txt$', filename).group(1)

    system_names = set([data_line[8] for data_line in parsed_data])

    mining_volume = sum([int(data_line[2]) for data_line in parsed_data])

    mining_price = sum([int(data_line[6]) for data_line in parsed_data])

    in_ve = len(system_names) == 1


    if not in_ve:
        raise Exception(f'{username} копал не в VE!')

    return {'volume': mining_volume,
            'price': mining_price,
            'name': username}


file_list = glob.glob('./*.txt')

# Заменяем обратные слеши на прямые
file_list = [f.replace('\\', '/') for f in file_list]

# Применяем функцию `parse_file` к каждому файлу
data_list = [parse_file(filename) for filename in file_list]
