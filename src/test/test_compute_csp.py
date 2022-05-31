import unittest

from algorithms.csp import compute_csp
from utils.file_reader import parse_json_dataset
from utils.heuristics import hf_distance, hf_duration, hf_duration_distance, hf_weighted_duration_distance

cities = parse_json_dataset('../../assets/dataset.json')


class TestComputeCSP(unittest.TestCase):
    # ----- ----- DISTANCE ----- ----- #
    def test_hp_distance_1(self):
        path, acc_weight = compute_csp(cities, 'Barcelona', 'Granollers', hf_distance)
        self.assertEqual(1010521, acc_weight)
        self.assertEqual(
            ['Barcelona', "L'Hospitalet de Llobregat", 'Mataró', 'Palamós', 'Blanes', 'Vic', 'Sort', 'Reus', 'Tremp',
             'Granollers'],
            list(map(lambda city: city.name, path)))

    def test_hp_distance_2(self):
        path, acc_weight = compute_csp(cities, 'Palamós', 'Sort', hf_distance)
        self.assertEqual(538290, acc_weight)
        self.assertEqual(['Palamós', 'Mataró', "L'Hospitalet de Llobregat", 'Blanes', 'Barcelona', 'Vic', 'Sort'],
                         list(map(lambda city: city.name, path)))

    # ----- ----- DURATION ----- ----- #
    def test_hp_duration_0(self):
        path, acc_weight = compute_csp(cities, 'Barcelona', 'Tremp', hf_duration)
        self.assertEqual(44394, acc_weight)
        self.assertEqual(
            ['Barcelona', "L'Hospitalet de Llobregat", 'Mataró', 'Palamós', 'Blanes', 'Vic', 'Sort', 'Reus', 'Tremp'],
            list(map(lambda city: city.name, path)))

    def test_hp_duration_1(self):
        path, acc_weight = compute_csp(cities, 'Barcelona', 'Granollers', hf_duration)
        self.assertEqual(53216, acc_weight)
        self.assertEqual(
            ['Barcelona', "L'Hospitalet de Llobregat", 'Mataró', 'Palamós', 'Blanes', 'Vic', 'Sort', 'Reus', 'Tremp',
             'Granollers'],
            list(map(lambda city: city.name, path)))

        def test_hp_duration_2(self):
            path, acc_weight = compute_csp(cities, 'Palamós', 'Sort', hf_duration)
            self.assertEqual(28545, acc_weight)
            self.assertEqual(['Palamós', 'Mataró', "L'Hospitalet de Llobregat", 'Blanes', 'Barcelona', 'Vic', 'Sort'],
                             list(map(lambda city: city.name, path)))

        # ----- ----- DURATION & DISTANCE ----- ----- #
        def test_hp_duration_distance_0(self):
            path, acc_weight = compute_csp(cities, 'Barcelona', 'Tremp', hf_duration_distance)
            self.assertEqual(6386190028, acc_weight)
            self.assertEqual(
                ['Barcelona', "L'Hospitalet de Llobregat", 'Mataró', 'Palamós', 'Blanes', 'Vic', 'Sort', 'Reus',
                 'Tremp'],
                list(map(lambda city: city.name, path)))

        def test_hp_duration_distance_1(self):
            path, acc_weight = compute_csp(cities, 'Barcelona', 'Granollers', hf_duration_distance)
            self.assertEqual(8082651806, acc_weight)
            self.assertEqual(
                ['Barcelona', "L'Hospitalet de Llobregat", 'Mataró', 'Palamós', 'Blanes', 'Vic', 'Sort', 'Reus',
                 'Tremp',
                 'Granollers'],
                list(map(lambda city: city.name, path)))

        def test_hp_duration_distance_2(self):
            path, acc_weight = compute_csp(cities, 'Palamós', 'Sort', hf_duration_distance)
            self.assertEqual(3278816794, acc_weight)
            self.assertEqual(['Palamós', 'Mataró', "L'Hospitalet de Llobregat", 'Blanes', 'Barcelona', 'Vic', 'Sort'],
                             list(map(lambda city: city.name, path)))

        # ----- ----- WEIGHTED DURATION & DISTANCE ----- ----- #
        def test_hp_weighted_duration_distance_0(self):
            path, acc_weight = compute_csp(cities, 'Barcelona', 'Tremp', hf_weighted_duration_distance)
            self.assertEqual(276542.4, acc_weight)
            self.assertEqual(
                ['Barcelona', "L'Hospitalet de Llobregat", 'Mataró', 'Palamós', 'Blanes', 'Vic', 'Sort', 'Reus',
                 'Tremp'],
                list(map(lambda city: city.name, path)))

        def test_hp_weighted_duration_distance_1(self):
            path, acc_weight = compute_csp(cities, 'Barcelona', 'Granollers', hf_weighted_duration_distance)
            self.assertEqual(340407.5, acc_weight)
            self.assertEqual(
                ['Barcelona', "L'Hospitalet de Llobregat", 'Mataró', 'Palamós', 'Blanes', 'Vic', 'Sort', 'Reus',
                 'Tremp',
                 'Granollers'],
                list(map(lambda city: city.name, path)))

        def test_hp_weighted_duration_distance_2(self):
            path, acc_weight = compute_csp(cities, 'Palamós', 'Sort', hf_weighted_duration_distance)
            self.assertEqual(181468.5, acc_weight)
            self.assertEqual(['Palamós', 'Mataró', "L'Hospitalet de Llobregat", 'Blanes', 'Barcelona', 'Vic', 'Sort'],
                             list(map(lambda city: city.name, path)))

    if __name__ == '__main__':
        unittest.main()
