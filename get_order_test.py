# Мельникова Анна,  10-я когорта — Финальный проект. Инженер по тестированию плюс
import requests
import configuration
import sender_stand_request

def test_get_order_by_track(): # тест на получение данных по номеру трека

    response = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER+'?t='+sender_stand_request.get_new_track())

    assert response.status_code == 200