import request_sender
import data

#Талабанова Ольга, 24 когорта - Финальный проект. Инженер по тестированию плюс

def test_get_order_by_track():
    track = request_sender.create_order()
    response = request_sender.get_order_details(trackNumber=track)
    assert response["order"] is not None
    order = response["order"]
    assert order["firstName"] == data.order_body["firstName"]
    assert order['phone'] == data.order_body["phone"]