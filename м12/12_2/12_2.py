import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
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


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers


class TournamentTest(unittest.TestCase):
    all_results = {}

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Усэйн', 10)
        self.runner2 = Runner('Андрей', 9)
        self.runner3 = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            print(result)

    def test_race_1(self):
        t = Tournament(90, self.runner1, self.runner3)
        results = t.start()
        self.all_results[len(results)] = results
        self.assertTrue(results[len(results)].name == 'Ник')

    def test_race_2(self):
        t = Tournament(90, self.runner2, self.runner3)
        results = t.start()
        self.all_results[len(results)] = results
        self.assertTrue(results[len(results)].name == 'Ник')

    def test_race_3(self):
        t = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = t.start()
        self.all_results[len(results)] = results
        self.assertTrue(results[len(results)].name == 'Ник')

if __name__ == "__main__":
    unittest.main()
