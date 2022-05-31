import unittest

from algorithms.a import compute_a
from utils.file_reader import parse_json_dataset
from utils.heuristics import hf_distance, hf_duration, hf_duration_distance, hf_weighted_duration_distance

cities = parse_json_dataset('../../assets/dataset.json')


class TestComputeA(unittest.TestCase):
    # ----- ----- DISTANCE ----- ----- #
    def test_hp_distance_0(self):
        path, acc_weight = compute_a(cities, 'Barcelona', 'Tremp', hf_distance)
        self.assertEqual(242752, acc_weight)
        self.assertEqual(['Barcelona', 'Vic', 'Tremp'],
                         list(map(lambda city: city.name, path)))

    def test_hp_distance_1(self):
        path, acc_weight = compute_a(cities, 'Barcelona', 'Granollers', hf_distance)
        self.assertEqual(32244, acc_weight)
        self.assertEqual(['Barcelona', 'Granollers'],
                         list(map(lambda city: city.name, path)))

    def test_hp_distance_2(self):
        path, acc_weight = compute_a(cities, 'Palamós', 'Sort', hf_distance)
        self.assertEqual(289436, acc_weight)
        self.assertEqual(['Palamós', 'Vic', 'Sort'],
                         list(map(lambda city: city.name, path)))

    # ----- ----- DURATION ----- ----- #
    def test_hp_duration_0(self):
        path, acc_weight = compute_a(cities, 'Barcelona', 'Tremp', hf_duration)
        self.assertEqual(11648, acc_weight)
        self.assertEqual(['Barcelona', 'Vic', 'Tremp'],
                         list(map(lambda city: city.name, path)))

    def test_hp_duration_1(self):
        path, acc_weight = compute_a(cities, 'Barcelona', 'Granollers', hf_duration)
        self.assertEqual(2302, acc_weight)
        self.assertEqual(['Barcelona', 'Granollers'],
                         list(map(lambda city: city.name, path)))

    def test_hp_duration_2(self):
        path, acc_weight = compute_a(cities, 'Palamós', 'Sort', hf_duration)
        self.assertEqual(15028, acc_weight)
        self.assertEqual(['Palamós', 'Vic', 'Sort'],
                         list(map(lambda city: city.name, path)))

    # ----- ----- DURATION & DISTANCE ----- ----- #
    def test_hp_duration_distance_0(self):
        path, acc_weight = compute_a(cities, 'Barcelona', 'Tremp', hf_duration_distance)
        self.assertEqual(1524579596, acc_weight)
        self.assertEqual(['Barcelona', 'Granollers', 'Vic', 'Tremp'],
                         list(map(lambda city: city.name, path)))

    def test_hp_duration_distance_1(self):
        path, acc_weight = compute_a(cities, 'Barcelona', 'Granollers', hf_duration_distance)
        self.assertEqual(74225688, acc_weight)
        self.assertEqual(['Barcelona', 'Granollers'],
                         list(map(lambda city: city.name, path)))

    def test_hp_duration_distance_2(self):
        path, acc_weight = compute_a(cities, 'Palamós', 'Sort', hf_duration_distance)
        self.assertEqual(1929385036, acc_weight)
        self.assertEqual(['Palamós', 'Blanes', 'Mataró', 'Granollers', 'Vic', 'Tremp', 'Sort'],
                         list(map(lambda city: city.name, path)))

    # ----- ----- WEIGHTED DURATION & DISTANCE ----- ----- #
    def test_hp_weighted_duration_distance_0(self):
        path, acc_weight = compute_a(cities, 'Barcelona', 'Tremp', hf_weighted_duration_distance)
        self.assertEqual(80979.2, acc_weight)
        self.assertEqual(['Barcelona', 'Vic', 'Tremp'],
                         list(map(lambda city: city.name, path)))

    def test_hp_weighted_duration_distance_1(self):
        path, acc_weight = compute_a(cities, 'Barcelona', 'Granollers', hf_weighted_duration_distance)
        self.assertEqual(11284.599999999999, acc_weight)
        self.assertEqual(['Barcelona', 'Granollers'],
                         list(map(lambda city: city.name, path)))

    def test_hp_weighted_duration_distance_2(self):
        path, acc_weight = compute_a(cities, 'Palamós', 'Sort', hf_weighted_duration_distance)
        self.assertEqual(97350.4, acc_weight)
        self.assertEqual(['Palamós', 'Vic', 'Sort'],
                         list(map(lambda city: city.name, path)))


if __name__ == '__main__':
    unittest.main()
