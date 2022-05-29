import unittest

from utils.error_manager import check_data_validity
from utils.file_reader import parse_json_dataset


class TestCheckDataValidity(unittest.TestCase):
    cities = parse_json_dataset('../../assets/dataset.json')

    def test_up_no_cities(self):
        with self.assertRaises(Exception):
            check_data_validity([], 'Barcelona', 'Granollers')

    def test_up_same_origin_and_destination(self):
        with self.assertRaises(Exception):
            check_data_validity(self.cities, 'Barcelona', 'Barcelona')

    def test_up_no_origin(self):
        with self.assertRaises(Exception):
            check_data_validity(self.cities, '', 'Barcelona')

    def test_up_no_destination(self):
        with self.assertRaises(Exception):
            check_data_validity(self.cities, 'Barcelona', '')

    def test_up_origin_not_in_dataset(self):
        with self.assertRaises(Exception):
            check_data_validity(self.cities, 'Lleida', 'Barcelona')

    def test_up_destination_not_in_dataset(self):
        with self.assertRaises(Exception):
            check_data_validity(self.cities, 'Barcelona', 'Lleida')

    def test_up_origin_and_destination_not_in_dataset(self):
        with self.assertRaises(Exception):
            check_data_validity(self.cities, 'Balaguer', 'Lleida')

    def test_hp_origin_and_destination_not_in_dataset(self):
        try:
            check_data_validity(self.cities, 'Barcelona', 'Granollers')
        except Exception:
            self.fail('check_data_validity() raised an Exception but it should have not.')


if __name__ == '__main__':
    unittest.main()
