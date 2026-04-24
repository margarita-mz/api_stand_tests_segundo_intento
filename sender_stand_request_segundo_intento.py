import configuration_segundo_intento
import requests
import data_segundo_intento

def get_docs():
    return requests.get(configuration_segundo_intento.URL_SERVICE + configuration_segundo_intento.DOC_PATH)

def get_logs():
    return requests.get(configuration_segundo_intento.URL_SERVICE + configuration_segundo_intento.LOG_MAIN_PATH,
                        params={"count": 20})

def get_users_table():
    return requests.get(configuration_segundo_intento.URL_SERVICE + configuration_segundo_intento.USERS_TABLE_PATH)


def post_new_user(body):
    return requests.post(configuration_segundo_intento.URL_SERVICE + configuration_segundo_intento.CREATE_USER_PATH,
                         json=body,
                         headers=data_segundo_intento.headers)

def post_products_kits(products_ids):
    return requests.post(configuration_segundo_intento.URL_SERVICE + configuration_segundo_intento.PRODUCTS_KITS_PATH,
                         json=products_ids,
                         headers=data_segundo_intento.headers)
