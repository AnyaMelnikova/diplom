import configuration
import requests
import data

def get_new_track(): #Создаем новый заказ, забираем оттуда номер заказа, изменяя его чиловое значение в строку
    if configuration.TRACK == "":
        response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.user_body,
                         headers=data.headers)

        track = response.json()['track']
        configuration.TRACK = str(track)
        return str(track)

    else:
        return configuration.TRACK



