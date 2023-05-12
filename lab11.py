def p1():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type

        def describe_restaurant(self):
            print(f'Название: {self.restaurant_name} Тип кухни: {self.cuisine_type}')

        def open_restaurant(self):
            print('Открыто с 10:00')



    newRestaurant = Restaurant(input(), input())
    print(newRestaurant.restaurant_name)
    print(newRestaurant.cuisine_type)

    newRestaurant.describe_restaurant()
    newRestaurant.open_restaurant()

    print('\n')

#p2():

    Restaurant1 = Restaurant('KFC', 'быстрое питание')
    Restaurant2 = Restaurant('Венеция', 'русская')
    Restaurant3 = Restaurant('Хочу-харчо', 'грузинская')

    Restaurant1.describe_restaurant()
    Restaurant2.describe_restaurant()
    Restaurant3.describe_restaurant()

    print('\n')
def p3():
    class Restaurant:
        def __init__(self, restaurant_name, cuisine_type, reiting):
            self.restaurant_name = restaurant_name
            self.cuisine_type = cuisine_type
            self.reiting = reiting

        def describe_restaurant(self):
            print(f'Название: {self.restaurant_name} Тип кухни: {self.cuisine_type}')

        def open_restaurant(self):
            print('Открыто!')

        def write_reiting(self):
            print(fr'Бывший рейтинг: {self.reiting}')
            self.reiting = input('Обновлённое значение: ')
            print(fr'Обновлено: {self.reiting}')

    newRestaurant = Restaurant('Невский Берег', 'русская', '5')
    newRestaurant.write_reiting()


p1(), p3()