import requests
import configuration
import data

def create_order():
    response = requests.post (configuration.ORDER_URL,
                              json = data.order_body)
    return response.json()['track']

def get_order_details(trackNumber):
    response = requests.get(configuration.ORDER_URL + "/track", params= {"t":trackNumber})
    return response.json ()




