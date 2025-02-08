# Григорий Климанов, 26-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request as SSR
import data

def test_order_can_be_taken_using_tracker():
    # Создание курьера
    SSR.create_courier(data.CREATE_COURIER_BODY)

    # Создание заказа
    order_response = SSR.create_order(data.CREATE_ORDER_BODY)

    # Работа с заказом
    order_track = order_response.json()['track']
    take_order_body = data.TAKE_ORDER_BY_NAME_BODY.copy() # Копирую глобульную переменную, чтобы издеваться над локальной
    take_order_body['t'] = str(order_track)
    
    # Принятие заказа
    take_order_response = SSR.take_order(take_order_body)
    
    assert take_order_response.status_code == 200, 'Order was not taken'
