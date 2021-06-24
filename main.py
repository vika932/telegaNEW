import requests
import json
import time
import const


def answer_user_bot(data):# отправка сообщения в чат
    data = {
       'chat_id': const.MY_ID,
       'text': data
    }
    url = const.URL.format(
        token=const.TOKEN,
        method=const.SEND_METH
    )
    response = requests.post(url, data=data)


def parse_weather_data(date):# прием данных и ввывод сообщения
    for elem in date['weather']:# пройтись по наличию данных
        weather_state = elem['main']
    temp = round(date['main']['temp'] - 273.15, 2)
    city = date['name']
    msg = f'погода в {city}: темпрература {temp}, сейчас {weather_state}'

    return msg


def get_weather(location):# обработка полученоого сообщения и вывод погоды
    url = const.WEATHER_URL.format(city=location,
                                   token=const.WEATHER_TOKEN)
    response = requests.get(url)
    if response.status_code != 200:# возврат сообщения 'город не найден, попробуйте снова'
        return 'город не найден, попробуйте снова'
    data = json.loads(response.content)#отправка данных на parse_weather_data
    return parse_weather_data(data)


def get_message(data): # сбор и системизация сообщения
    return data['message']['text']


def save_update_id(update): # сохрание в файл update_id
    with open(const.UPDATE_ID_FILE_PATH, 'w') as file:
        file.write(str(update['update_id']))
    const.UPDATE_ID = update['update_id']
    return True


def main():
    while True:
        url = const.URL.format(token=const.TOKEN, method=const.UPDATE_METH) #отправка запроса
        content = requests.get(url).text # поллучение ответа взятие текста

        data = json.loads(content) # преобразование из сторики в словарь
        result = data['result'][::-1] # сортировка в обратном порядке
        needed_part = None

        for elem in result: # проходим по всем id находим наш id и сохранияем его в переменной
            if elem['message']['chat']['id'] == const.MY_ID:
                needed_part = elem
                break

        if const.UPDATE_ID != needed_part['update_id']:
            message = get_message(needed_part)
            msg = get_weather(message)
            answer_user_bot(msg)
            save_update_id(needed_part)

        time.sleep(1)


if __name__ == '__main__': #  выполнение кода когда файл напрямую запущен
    main()
