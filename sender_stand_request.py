# Здесь хранятся основные функции, которые могут использовать в нескольких автотестах

import requests

import configuration

def create_courier(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_COURIER_PATH,
                         json=body)

def create_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, 
                         json=body)

def take_order(body):
    return requests.get(configuration.URL_SERVICE + configuration.TAKE_ORDER_BY_TRACK,
                                        params=body)
