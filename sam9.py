class Tomato:
    # Статическое свойство со стадиями созревания
    states = {
        0: 'Отсутствует',
        1: 'Цветение',
        2: 'Зеленый',
        3: 'Красный'
    }

    def __init__(self, index):
        # Динамические свойства: _index и _state
        self._index = index
        self._state = 0  # Начинаем с отсутствия созревания

    def grow(self): # если стадия меньше 3, то к стадии прибавляем 1
        if self._state < 3:
            self._state += 1

    def is_ripe(self): # True если 3 стадия
        return self._state == 3

class TomatoBush:
    def __init__(self, num_tomatoes):
        # Создаем список томатов в зависимости от количества
        self.tomatoes = [Tomato(index) for index in range(1, num_tomatoes + 1)]

    def grow_all(self): # для каждого помидора в списке
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self): # True, если все помидоры созрели
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self): #Очищает список помидоров
        self.tomatoes = []

class Gardener:
    def __init__(self, name, plant):
        # Динамические свойства: name и _plant
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self): #Проверяет, все ли помидоры созрели, собирает урожай, если он созрел, и выводит результат.
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собран.")
        else:
            print("Урожай еще не созрел.")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:")
        print("1. Создайте объект класса TomatoBush с указанием количества томатов.")
        print("2. Создайте объект класса Gardener с указанием имени и растения (TomatoBush).")
        print("3. Используйте метод work() садовника для ухода за растением.")
        print("4. Используйте метод harvest() для сбора урожая, когда все томаты созрели.")

# Теперь, давайте проведем тесты:
if __name__ == "__main__":
    Gardener.knowledge_base()  # Вызов справки по садоводству

    # Создаем куст с 3 томатами
    tomato_bush = TomatoBush(3)

    # Создаем садовника по имени "Alice" и привязываем его к кусту
    gardener = Gardener("Alice", tomato_bush)

    # Садовник работает
    gardener.work()

    # Попробуем собрать урожай (так как томаты еще не созрели)
    gardener.harvest()

    # Продолжаем ухаживать за кустом
    gardener.work()





    # Проверяем созрели ли все томаты
    if tomato_bush.all_are_ripe():
        print("Все томаты созрели.")
        gardener.harvest()
    else:
        print("Томаты еще не все созрели.")

    # Создаем новый куст с 2 томатами
    tomato_bush2 = TomatoBush(2)

    # Создаем садовника по имени "Bob" и привязываем его ко второму кусту
    gardener2 = Gardener("Bob", tomato_bush2)

    # Садовник работает
    gardener2.work()

    # Продолжаем ухаживать за ко вторым кустом
    gardener2.work()

    gardener2.work()



    # Проверяем созрели ли все томаты на втором кусте
    if tomato_bush2.all_are_ripe():
        print("Все томаты на втором кусте созрели.")
        gardener2.harvest()
    else:
        print("Томаты на втором кусте еще не все созрели.")

