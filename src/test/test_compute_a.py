import unittest

from algorithms.a import compute_a
from model.connection import Connection
from utils.file_reader import parse_json_dataset


def hf_distance(c: Connection) -> int:
    return c.distance


def hf_duration(c: Connection) -> int:
    return c.duration


def hf_duration_distance(c: Connection) -> int:
    return c.duration * c.distance


def hf_weighted_duration_distance(c: Connection) -> float:
    return 0.7 * c.duration + 0.3 * c.distance


class TestComputeA(unittest.TestCase):
    cities = parse_json_dataset('../../assets/dataset.json')

    # ----- ----- DISTANCE ----- ----- #
    def test_hp_distance_0(self):
        path, acc_weight = compute_a(self.cities, 'Barcelona', 'Tremp', hf_distance)
        self.assertEqual(acc_weight, 242752)
        self.assertEqual(list(map(lambda city: city.name, path)),
                         ['Barcelona', 'Vic', 'Tremp'])

    def test_hp_distance_1(self):
        path, acc_weight = compute_a(self.cities, 'Barcelona', 'Granollers', hf_distance)
        self.assertEqual(acc_weight, 32244)
        self.assertEqual(list(map(lambda city: city.name, path)),
                         ['Barcelona', 'Granollers'])

    def test_hp_distance_2(self):
        path, acc_weight = compute_a(self.cities, 'Palamós', 'Sort', hf_distance)
        self.assertEqual(acc_weight, 289436)
        self.assertEqual(list(map(lambda city: city.name, path)),
                         ['Palamós', 'Vic', 'Sort'])

    # ----- ----- DURATION ----- ----- #
    def test_hp_duration_0(self):
        path, acc_weight = compute_a(self.cities, 'Barcelona', 'Tremp', hf_duration)
        self.assertEqual(acc_weight, 11648)
        self.assertEqual(list(map(lambda city: city.name, path)),
                         ['Barcelona', 'Vic', 'Tremp'])

    def test_hp_duration_1(self):
        path, acc_weight = compute_a(self.cities, 'Barcelona', 'Granollers', hf_duration)
        self.assertEqual(acc_weight, 2302)
        self.assertEqual(list(map(lambda city: city.name, path)),
                         ['Barcelona', 'Granollers'])

    def test_hp_duration_2(self):
        path, acc_weight = compute_a(self.cities, 'Palamós', 'Sort', hf_duration)
        self.assertEqual(acc_weight, 15028)
        self.assertEqual(list(map(lambda city: city.name, path)),
                         ['Palamós', 'Vic', 'Sort'])

    # ----- ----- DURATION & DISTANCE ----- ----- #
    def test_hp_duration_distance_0(self):
        path, acc_weight = compute_a(self.cities, 'Barcelona', 'Tremp', hf_duration_distance)
        self.assertEqual(acc_weight, 1524579596)
        self.assertEqual(list(map(lambda city: city.name, path)),
                         ['Barcelona', 'Granollers', 'Vic', 'Tremp'])

    def test_hp_duration_distance_1(self):
        path, acc_weight = compute_a(self.cities, 'Barcelona', 'Granollers', hf_duration_distance)
        self.assertEqual(acc_weight, 74225688)
        self.assertEqual(list(map(lambda city: city.name, path)),
                         ['Barcelona', 'Granollers'])

    def test_hp_duration_distance_2(self):
        path, acc_weight = compute_a(self.cities, 'Palamós', 'Sort', hf_duration_distance)
        self.assertEqual(acc_weight, 1929385036)
        self.assertEqual(list(map(lambda city: city.name, path)),
                         ['Palamós', 'Blanes', 'Mataró', 'Granollers', 'Vic', 'Tremp', 'Sort'])

    # ----- ----- WEIGHTED DURATION & DISTANCE ----- ----- #
    def test_hp_weighted_duration_distance_0(self):
        path, acc_weight = compute_a(self.cities, 'Barcelona', 'Tremp', hf_weighted_duration_distance)
        self.assertEqual(acc_weight, 80979.2)
        self.assertEqual(list(map(lambda city: city.name, path)),
                         ['Barcelona', 'Vic', 'Tremp'])

    def test_hp_weighted_duration_distance_1(self):
        path, acc_weight = compute_a(self.cities, 'Barcelona', 'Granollers', hf_weighted_duration_distance)
        self.assertEqual(acc_weight, 11284.599999999999)
        self.assertEqual(list(map(lambda city: city.name, path)),
                         ['Barcelona', 'Granollers'])

    def test_hp_weighted_duration_distance_2(self):
        path, acc_weight = compute_a(self.cities, 'Palamós', 'Sort', hf_weighted_duration_distance)
        self.assertEqual(acc_weight, 97350.4)
        self.assertEqual(list(map(lambda city: city.name, path)),
                         ['Palamós', 'Vic', 'Sort'])


if __name__ == '__main__':
    unittest.main()
