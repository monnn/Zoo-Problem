import unittest
from animal import Animal


class TestAnimal(unittest.TestCase):

    def setUp(self):
        self.animal = Animal('Snake', 'Pypy', 12, 'male', 63)

    def test_animal_init(self):
        self.assertEqual(self.animal.species, 'Snake')
        self.assertEqual(self.animal.name, 'Pypy')
        self.assertEqual(self.animal.age, 12)
        self.assertEqual(self.animal.weight, 63)

    def test_animal_eat(self):
        self.animal.eat()
        self.assertEqual(self.animal.weight, 66.15)

    def test_animal_grow(self):
        self.animal.grow()
        self.assertEqual(self.animal.age, 13)
        self.assertEqual(self.animal.weight, 64.26)

    def test_animal_dies(self):
        result = []
        for i in range(100):
            result.append(self.animal.is_dead())
        self.assertIn(True, result)
        self.assertIn(False, result)


if __name__ == '__main__':
    unittest.main()
