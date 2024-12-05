import requests
import configuration
import data

def create_order():
    response = requests.post (configuration.ORDER_URL,
                              json = data.order_body)
    return response.json()['track']

def get_order_details(track_number):
    response = requests.get(configuration.ORDER_URL + "/track", params={"t": track_number})
    return response

