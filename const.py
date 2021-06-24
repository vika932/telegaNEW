TOKEN ='1884007346:AAFFCHaztjjsVJFw6a7ZZPP1VywF3F0lZXw'

URL = 'https://api.telegram.org/bot{token}/{method}'


UPDATE_METH = 'getUpdates'
SEND_METH = 'sendMessage'


MY_ID = 847822770 # вводить свой  id Вы можете узнать свой ID в телеграмм онлайн с помощью бота Get any telegram ID

UPDATE_ID_FILE_PATH = 'update_id'

with open(UPDATE_ID_FILE_PATH) as file: #проверка на пустую часть
    data = file.readline()
    if data:
        data = int(data)
    UPDATE_ID = data

WEATHER_TOKEN = '877e2fe4792d2b20b2682d7e02b1cddc'

WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'
