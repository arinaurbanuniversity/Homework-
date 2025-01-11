import unittest
import logging

class Runner:
    def __init__(self, name, speed=5):
        if not isinstance(name, str):
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.name = name
        self.distance = 0
        if speed < 0:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    filename='runner_tests.log',
    encoding='utf-8',
    filemode='w'
)

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            runner = Runner('Тест', -5)
            runner.walk()
            logging.info('"test_walk" выполнен успешно')
        except ValueError as e:
            logging.warning(f'Неверная скорость для Runner: {e}')
            logging.error(f'Traceback: {e.__traceback__}')

    def test_run(self):
        try:
            runner = Runner(123, 5)
            runner.run()
            logging.info('"test_run" выполнен успешно')
        except TypeError as e:
            logging.warning(f'Неверный тип данных для объекта Runner: {e}')
            logging.error(f'Traceback: {e.__traceback__}')


if __name__ == '__main__':
    unittest.main()