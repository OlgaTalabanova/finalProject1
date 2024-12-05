# Практический блок: вторая часть
# Работа с базой данных
- Задание 1
  Проверить отображение созданного заказа в базе данных. 
  Нужно вывести список логинов курьеров с количеством заказов в статусе в доставке (inDelivery = true).
- Задание 2
  Проверить, что статусы заказов записываются в базу правильно. 
  Нужно вывести все трекеры заказов и их статусы.
  Статусы определяются по следующему правилу:
  Если поле finished == true, то вывести статус 2.
  Если поле canсelled == true, то вывести статус -1.
  Если поле inDelivery == true, то вывести статус 1.
  Для остальных случаев вывести 0.
  
  
  
# Автоматизация теста к API
Клиент создает заказ. Тест проверяет, что по треку заказа можно получить данные о заказе   
