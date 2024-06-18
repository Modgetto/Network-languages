import requests
cities = [
    'Омск',
    'Калининград',
    'Челябинск',
    'Владивосток',
    'Красноярск',
    'Москва',
    'Екатеринбург'
]
def make_url(city):
    # в URL задаём город, в котором узнаем погоду
    return f'http://wttr.in/{city}'
def make_parameters():
    params = {
        'format': 2,  # погода одной строкой
        'M': ''  # скорость ветра в "м/с"
    }
    return params
def what_weather(city):
    try:
        url = make_url(city)
        params = make_parameters()
        response = requests.get(url, params=params)
        if response.status_code == 200:
            return response.text.strip()
        else:
            return '<Ошибка на сервере погоды>'
    except requests.ConnectionError:
        return '<Сетевая ошибка>'
print('Погода в городах:')
for city in cities:
    print(city, what_weather(city))
