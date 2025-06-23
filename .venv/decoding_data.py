import shelve

FILENAME = 'filament'
FILENAMEPERSONAL = 'personal'

class Filament:
    def __init__(self, name, weight, prise, reject):
        self.name = name
        self.weight = weight
        self.prise = prise
        self.reject = reject

class Personal:
    def __init__(self, prise):
        self.prise = prise

def read_filament():
    with shelve.open(FILENAME) as shelf:
        shelf['ABS'] = Filament('ABS', 1000, 1990, 80)
        shelf['PLA'] = Filament('PLA', 1000, 2390, 20)
        shelf['PETG'] = Filament('PETG', 1000, 1990, 20)
        shelf['TPU'] = Filament('TPU', 500, 2790, 20)
        shelf['PC'] = Filament('PC', 500,2190,80)
        shelf['Nulon'] = Filament('Nulon', 500, 5300,80)
    return

def read_personal():
    with shelve.open(FILENAMEPERSONAL) as shelf:
        shelf['Printer power consumption'] = Personal(200)  # Потребление принтера в ватах
        shelf['The cost of light'] = Personal(3.4)  # Цена 1 КвТ в час
        shelf['The cost of renting a room'] = Personal(20000)  # Стоймость аренды помещения
        shelf['Percentage of time'] = Personal(15)  # Добавляет процент ко времени печати
        shelf['Percentage of weight'] = Personal(5)  # Добавляет процент к весу печати
        shelf['Interest on consumables'] = Personal(3)  # Добавляет процент на расходники
        shelf['Interest on depreciation'] = Personal(10)  # Добавляет процент на амортизацию
        shelf['Profit'] = Personal(70)  # Устанавливает процент на чистую прибыль
    return

# Перебирает все возможные филаменты
def search_filament():
    open_filament = []
    with shelve.open(FILENAME) as shelf:
        for filament in shelf.keys():
            open_filament.append(filament)
    open_filament.sort()
    return open_filament

# Добавление или изменение существующего филамента
def add_filament(name_filament, weight_filament, prise_filament, reject_filament):
    with shelve.open(FILENAME) as shelf:
        shelf[name_filament] = Filament(name_filament, weight_filament, prise_filament, reject_filament)
    return print('Новый филамент добавлен')

# Изменение даанных в персональном
def change_personal(name_personal, prise_personal):
    with shelve.open(FILENAMEPERSONAL) as shelf:
        shelf[name_personal] = Personal(prise_personal)
    return print('Данные изменены')

# Для запроса данных из филаментов
def load_filament(name_filament, request):
    with shelve.open(FILENAME) as shelf:
        load_filament = shelf[name_filament]
        if request == 'weight':
            return load_filament.weight
        elif request == 'prise':
            return load_filament.prise
        elif request == 'reject':
            return load_filament.reject
    return print('Неверный запрос')

# Для запроса данных из персонального файла
def load_personal(name_personal):
    with shelve.open(FILENAMEPERSONAL) as shelf:
        loading_personal = shelf[name_personal]
    return loading_personal.prise

# Удаление филамента
def del_filament(name_filament):
    with shelve.open(FILENAME) as shelf:
        shelf.pop(name_filament,'NotFound')
        return print('Филамент удален')