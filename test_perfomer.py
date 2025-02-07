import configuration
import data

import requests

def create_courier(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_COURIER_PATH,
                         json=body)

def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, 
                         json=body)

def test_order_can_be_taken_using_tracker():
    # Создание курьера
    courier_response = create_courier(data.CREATE_COURIER_BODY)
    assert courier_response.status_code == 201, 'Courier was not made' 

    # Создание заказа
    order_response = create_order(data.CREATE_ORDER_BODY)
    assert order_response.status_code == 201, 'Order was not made'

    # Работа с заказом
    order_track = order_response.json()['track']
    take_order_body = data.TAKE_ORDER_BY_NAME_BODY.copy() # Копирую глобульную переменную, чтобы издеваться над локальной
    take_order_body['t'] = str(order_track)
    
    # Принятие заказа
    take_order_response = requests.get(configuration.URL_SERVICE + configuration.TAKE_ORDER_BY_TRACK,
                                        params=take_order_body)
    assert take_order_response.status_code == 200, 'Order was not taken'
