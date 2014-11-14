import random
import json


class Animal(object):

    DEAD_RATIO = 0.8
    DEAD_CHANCE_RATIO = 0.8
    LIFE_EXPECTANCIES = {'Snake': 12,
                         'Horse': 30,
                         'Wolf': 25,
                         'Tiger': 24,
                         'Bear': 40
                         }
    AVERAGE_WEIGHTS = {'Snake': 65,
                       'Horse': 280,
                       'Wolf': 60,
                       'Tiger': 180,
                       'Bear': 400}

    def __init__(self, species, name, age, gender, weight):
        self.species = species
        self.age = age
        self.name = name
        self.gender = gender
        self.weight = weight

    def can_eat(self):
        if self.species in Animal.AVERAGE_WEIGHTS:
            average_weight = Animal.AVERAGE_WEIGHTS[self.species]
            if average_weight < self.weight:
                return True
            else:
                return False

    def grow(self):
        self.age += 1
        self.weight += self.weight * 0.1

    def eat(self):
        if self.can_eat():
            self.weight += 0.5
        else:
            return

    def chance_to_die(self):
        if self.species in Animal.LIFE_EXPECTANCIES:
            life_expectancy = Animal.LIFE_EXPECTANCIES[self.species]
            return self.age / life_expectancy

    def is_dead(self):
        if self.chance_to_die() > Animal.DEAD_RATIO:
            if random.random() > Animal.DEAD_CHANCE_RATIO:
                return True
        return False

    def __str__(self):
        return "{0}: {1}  {2} months  {3} kg".format(
            self.name,
            self.species,
            self.age,
            self.weight)

    def load_config(self, file_name):
        config = open(file_name, 'r')
        data = json.loads(config.read())
        config.close()
        return data

    # def jsonify(self, instance):
    #     fp = open('animals.json', 'a+')
    #     data = json.dumps(str(instance.__dict__), indent=4, sort_keys=True)
    #     fp.write(data)
    #     fp.close()

# a = Animal('Snake', 'Pesho', 12, 'male', 43)
# # print(a)
# # print(a.is_dead())
# data = a._load_config('config.json')
# print(eval(data['animals']))

