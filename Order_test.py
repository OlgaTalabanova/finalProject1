import requests
import request_sender
import data
import configuration

#Талабанова Ольга, 24 когорта - Финальный проект. Инженер по тестированию плюс



def test_get_order_by_track():
    def get_order_details(trackNumber):
        response = requests.get(configuration.ORDER_URL + "/track", params={"t": trackNumber})
        assert response.status_code == 200
        return response.json()

    track = request_sender.create_order()
    response = get_order_details(trackNumber=track)
    order = response["order"]




