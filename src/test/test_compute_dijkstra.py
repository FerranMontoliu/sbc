import unittest

from algorithms.dijkstra import compute_dijkstra
from utils.file_reader import parse_json_dataset
from utils.heuristics import hf_distance, hf_duration, hf_duration_distance, hf_weighted_duration_distance

cities = parse_json_dataset('../../assets/dataset.json')


class TestComputeDijkstra(unittest.TestCase):
    # ----- ----- DISTANCE ----- ----- #
    def test_hp_distance_0(self):
        solution = compute_dijkstra(cities, 'Barcelona', hf_distance)
        self.assertEqual({'Barcelona': 0,
                          'Granollers': 32244,
                          "L'Hospitalet de Llobregat": 8369,
                          'Mataró': 32157,
                          'Vic': 71048,
                          'Palamós': 117897,
                          'Tremp': 242752,
                          'Sort': 256848,
                          'Reus': 240309,
                          'Blanes': 71298
                          },
                         solution)

    # ----- ----- DURATION ----- ----- #
    def test_hp_duration_0(self):
        solution = compute_dijkstra(cities, 'Barcelona', hf_duration)
        self.assertEqual({'Barcelona': 0,
                          'Blanes': 3641,
                          'Granollers': 2302,
                          "L'Hospitalet de Llobregat": 1478,
                          'Mataró': 2313,
                          'Palamós': 5281,
                          'Reus': 10589,
                          'Sort': 14379,
                          'Tremp': 11648,
                          'Vic': 3798},
                         solution)

    # ----- ----- DURATION & DISTANCE ----- ----- #
    def test_hp_duration_distance_0(self):
        solution = compute_dijkstra(cities, 'Barcelona', hf_duration_distance)
        self.assertEqual({'Barcelona': 0,
                          'Blanes': 234992976,
                          'Granollers': 74225688,
                          "L'Hospitalet de Llobregat": 12369382,
                          'Mataró': 74379141,
                          'Palamós': 394375450,
                          'Reus': 1326154647,
                          'Sort': 1711059716,
                          'Tremp': 1524579596,
                          'Vic': 176703196},
                         solution)

    # ----- ----- WEIGHTED DURATION & DISTANCE ----- ----- #
    def test_hp_weighted_duration_distance_0(self):
        solution = compute_dijkstra(cities, 'Barcelona', hf_weighted_duration_distance)
        self.assertEqual({'Barcelona': 0,
                          'Blanes': 23938.1,
                          'Granollers': 11284.599999999999,
                          "L'Hospitalet de Llobregat": 3545.2999999999997,
                          'Mataró': 11266.2,
                          'Palamós': 39065.799999999996,
                          'Reus': 79504.99999999999,
                          'Sort': 87119.7,
                          'Tremp': 80979.2,
                          'Vic': 23972.999999999996},
                         solution)


if __name__ == '__main__':
    unittest.main()
