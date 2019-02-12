# EASY
# Задача - 1
# Опишите несколько классов TownCar, SportCar, WorkCar, PoliceCar
# У каждого класса должны быть следующие аттрибуты:
# speed, color, name, is_police - Булево значение.
# А так же несколько методов: go, stop, turn(direction) - которые должны сообщать,
#  о том что машина поехала, остановилась, повернула(куда)
# Задача - 2
# Посмотрите на задачу-1 подумайте как выделить общие признаки классов
# в родительский и остальные просто наследовать от него.

class TownCar:

    # конструктор класса
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Осторожно - Полиция!!' if self.is_police == True else '{} поехал(а)!'.format(self.name))

    def stop(self):
        print('{} остановился(ась)'.format(self.name))

    def turn(self, direction):
        print('{} повернул(а) {}'.format(self.name, direction))


class SportCar(TownCar):
    def __init__(self, speed, color, name, is_police, max_speed):
        TownCar.__init__(self, speed, color, name, is_police)
        self.max_speed = max_speed


class WorkCar(TownCar):
    def __init__(self, speed, color, name, is_police, max_weight):
        TownCar.__init__(self, speed, color, name, is_police)
        self.max_weight = max_weight


class PoliceCar(TownCar):
    def __init__(self, speed, color, name, is_police, number):
        TownCar.__init__(self, speed, color, name, is_police)
        self.number = number

    def signal(self):
        print('УУУУуууу'.format(self.name))


car_1 = TownCar(120, 'белый', 'Ford', False)
car_2 = PoliceCar(150, 'синяя', 'Jaguar', True, '11-23')
car_1.stop()
car_2.go()
car_2.signal()
car_2.turn('направо')


# MEDIUM
# Задача - 1
# Ранее мы с вами уже писали игру, используя словари в качестве
# структур данных для нашего игрока и врага, давайте сделаем новую, но уже с ООП
# Опишите базовый класс Person, подумайте какие общие данные есть и у врага и у игрока
# Не забудьте, что у них есть помимо общих аттрибутов и общие методы.
# Теперь наследуясь от Person создайте 2 класса Player, Enemy.
# У каждой сущности должы быть аттрибуты health, damage, armor
# У каждой сущности должно быть 2 метода, один для подсчета урона, с учетом брони противника,
# второй для атаки противника.
# Функция подсчета урона должна быть инкапсулирована
# Вам надо описать игровой цикл так же через класс.
# Создайте экземпляры классов, проведите бой. Кто будет атаковать первым оставляю на ваше усмотрение.

import random


class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def _calculate_damage(self, damage):
        if self.armor > 0:
            self.armor = self.armor - int(damage * random.randrange(1, 5))
            if self.armor <= 0:
                self.armor = 0
        else:
            self.health = self.health - int(damage * random.randrange(1, 5))
            if self.health <= 0:
                self.health = 0
        print('{} получил урон. Его здоровье: {} единиц'.format(self.name, self.health))

    def attack(self, person):
        person._calculate_damage(self.damage)


class Player(Person):

    def __init__(self, name, health, damage, armor):
        Person.__init__(self, name, health, damage, armor)


class Enemy(Person):

    def __init__(self, name, health, damage, armor):
        Person.__init__(self, name, health, damage, armor)


class Play:
    def __init__(self, person1, person2):
        self.person1 = person1
        self.person2 = person2
    print('Бой начался!')

    def start(self, person1, person2):
        while person1.health > 0 and person2.health > 0:
            person1.attack(person2)
            if person2.health == 0:
                print('{} победил!'.format(person1.name))
                break
            person2.attack(person1)
            if person1.health == 0:
                print('{} победил!'.format(person2.name))

player = Player('Максим', 100, 10, 5)
enemy = Enemy('Женя', 100, 8, 5)

fight = Play(player,enemy)
fight.start(player,enemy)