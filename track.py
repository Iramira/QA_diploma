# Ирина Булдакова, 10 когорта, финальный проект, "Инженер по тестированию плюс". Приложение "Яндекс Самокат"

import sending_requests
# Получение заказа по номеру трека
def get_track_number_of_order():
    track_number = sending_requests.post_new_order()
    print(track_number.json())
    return track_number.json() ["track"]
# Проверка получения в ответе кода 200
def test_create_track_order():
    track_number = get_track_number_of_order()
    get_response = sending_requests.get_order_info(track_number)
    assert get_response.status_code == 200

