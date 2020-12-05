import unittest
from seat_finder import find_row_from_code
from seat_finder import find_seat_from_code
from seat_finder import find_seat_id_from_code

class TestSeatFinder(unittest.TestCase):

    def test_find_row_from_code(self):
        self.assertEqual(44, find_row_from_code('FBFBBFF'))

    def test_find_seat_from_code(self):
        self.assertEqual(5, find_seat_from_code('RLR'))

    def test_find_seat_id_from_code(self):
        self.assertEqual(567, find_seat_id_from_code('BFFFBBFRRR'))
        self.assertEqual(119, find_seat_id_from_code('FFFBBBFRRR'))
        self.assertEqual(820, find_seat_id_from_code('BBFFBBFRLL'))

if __name__ == '__main__':
    unittest.main()
