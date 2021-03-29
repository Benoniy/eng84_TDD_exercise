import unittest
import naan_factory


class NaanTest(unittest.TestCase):
    factory_naan = naan_factory.NaanFactory()  # Instantiate NaanFactory

    def test_make_dough(self):
        self.assertEqual(self.factory_naan.make_dough("flour", "water"), "dough")  # Checks if correct input for make_dough returns "dough"

    def test_bake_dough(self):
        self.assertEqual(self.factory_naan.bake_dough("dough"), "naan bread")  # Checks if correct input for bake_dough returns "naan bread"

    def test_run_factory(self):
        self.assertEqual(self.factory_naan.run_factory("flour", "water"), "naan bread")  # Checks if correct input for run_factory returns "naan bread"

    def test_make_dough_wrong(self):
        self.assertEqual(self.factory_naan.make_dough("water", "salt"), "watery salt")  # Checks if incorrect input for make_dough returns the correct mistake

    def test_bake_dough_wrong(self):
        self.assertEqual(self.factory_naan.bake_dough("salt"), "unknown")  # Checks if incorrect input for bake_dough returns "unknown"

    def test_run_factory_wrong(self):
        self.assertEqual(self.factory_naan.run_factory("batter", "water"), "unknown")  # Checks if incorrect input for run_factory returns "unknown"
