import decoding_data

# Расшифровка времени из дни:часы:минуты в минуты
def time_decoding(time):
    day = int(time[0:2])
    hour = int(time[3:5])
    min = int(time[6:8])
    time = ((day * 24) + hour) * 60 + min
    return time #Доработать при отсутствии каих либо цифр ставить нули

# Цена за 1 грамм пластика с учетом брака (Вес)
def prise_filament(name_filament):
    weight = decoding_data.load_filament(name_filament, 'weight')
    prise = decoding_data.load_filament(name_filament, 'prise')
    reject = decoding_data.load_filament(name_filament, 'reject')
    gram = prise / weight
    return round(gram + (gram * reject / 100),2)

# Цена электричества за 1 минуту печати (Время)
def prise_elektric_power():
    printer = decoding_data.load_personal('Printer power consumption')
    electric = decoding_data.load_personal('The cost of light')
    return round(((printer / 1000) * electric) / 60 , 3)

# Цена аренды помещения в 1 минуту печати (Время)
def prise_renting():
    renting = decoding_data.load_personal('The cost of renting a room')
    return round(renting / 30 / 24 / 60 , 2)

# Расчет времени на печать (время + 15%) (Время)
def time_print(time_model):
    percentage_of_time = decoding_data.load_personal('Percentage of time')
    return time_model + time_model * (percentage_of_time / 100)

# Вес + 5% (Вес)
def weight_print(weight_model):
    percentage_of_weight = decoding_data.load_personal('Percentage of weight')
    return weight_model + weight_model * (percentage_of_weight / 100)

# Прибыль = цена + 100% (Время + Вес)
def profit(prise_model):
    percentage_on_profit = decoding_data.load_personal('Profit')
    return prise_model * (percentage_on_profit / 100)

# Расходники и амартизация (3%+10% от заказа) (Время + Вес)
def consumables_and_depreciation(prise_model):
    interest_on_consumables = decoding_data.load_personal('Interest on consumables')
    interest_on_depreciation = decoding_data.load_personal('Interest on depreciation')
    return prise_model * ((interest_on_consumables + interest_on_depreciation) / 100)

# Скидка (Прибыль)
def sale_print(prise_model, size_of_sale):
    if size_of_sale == 0 or size_of_sale == '':
        return prise_model
    return prise_model - prise_model * (size_of_sale / 100)

# Основная фунция расчета
def calc_print(name_filament, time_model, weight_model, psi_model, sale_prise):
    weight_calculation = weight_print(weight_model) * prise_filament(name_filament)
    # Расчет вес + процент умноженый на стоймость филамента за грамм
    time_calculation = time_print(time_model)  # Расчет время + процент
    prise_time_elektric = time_calculation * prise_elektric_power()  # Расчет за электроэнергию
    prise_time_renting = time_calculation * prise_renting()  # Расчет за аренду помещения
    prise_weight_and_time = weight_calculation + prise_time_elektric + prise_time_renting  # Стоймость вес + время
    prise_not_sale = (prise_weight_and_time + consumables_and_depreciation(prise_weight_and_time) + profit(prise_weight_and_time)) * psi_model  # Расчет без скидки
    return round(sale_print(prise_not_sale, sale_prise), 2)