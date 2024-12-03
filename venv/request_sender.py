import requests
import configuration
import data

def create_order():
    response = requests.post (configuration.ORDER_URL,
                              json = data.order_body)
    return response.json()['track']






