import requests
import request_sender

#Талабанова Ольга, 24 когорта - Финальный проект. Инженер по тестированию плюс



def test_get_order_by_track():
    track_number = request_sender.create_order()
    response = request_sender.get_order_details(track_number)
    assert response.status_code == 200
