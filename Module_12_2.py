import Runner_and_Tournament
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner_and_Tournament.Runner("Усэйн", 10)
        self.runner2 = Runner_and_Tournament.Runner("Андрей", 9)
        self.runner3 = Runner_and_Tournament.Runner("Ник", 3)

    def tearDown(self):
        print(self.all_results)
        self.all_results.clear()

    def test_1(self):
        tournament = Runner_and_Tournament.Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        max_key = max(self.all_results.keys())
        last_runner_name = self.all_results[max_key]
        self.assertEqual(last_runner_name, "Ник")

    def test_2(self):
        tournament = Runner_and_Tournament.Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        max_key = max(self.all_results.keys())
        last_runner_name = self.all_results[max_key]
        self.assertEqual(last_runner_name, "Ник")

    def test_3(self):
        tournament = Runner_and_Tournament.Tournament(90, self.runner2, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        max_key = max(self.all_results.keys())
        last_runner_name = self.all_results[max_key]
        self.assertEqual(last_runner_name, "Ник")

    def test_4(self):
        tournament = Runner_and_Tournament.Tournament(6, self.runner3, self.runner1)
        results = tournament.start()
        self.all_results.update(results)
        max_key = max(self.all_results.keys())
        last_runner_name = self.all_results[max_key]
        self.assertEqual(last_runner_name, "Ник")


if __name__ == '__main__':
    unittest.main()
