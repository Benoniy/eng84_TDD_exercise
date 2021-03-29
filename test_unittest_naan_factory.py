import unittest
import naan_factory


class NaanTest(unittest.TestCase):
    factory_naan = naan_factory.NaanFactory()

    def test_make_dough(self):
        self.assertEqual(self.factory_naan.make_dough("flour", "water"), "dough")

    def test_bake_dough(self):
        self.assertEqual(self.factory_naan.bake_dough("dough"), "naan bread")

    def test_run_factory(self):
        self.assertEqual(self.factory_naan.run_factory("flour", "water"), "naan bread")

    def test_make_dough_wrong(self):
        self.assertEqual(self.factory_naan.make_dough("water", "salt"), "watery salt")

    def test_bake_dough_wrong(self):
        self.assertEqual(self.factory_naan.bake_dough("salt"), "unknown")

    def test_run_factory_wrong(self):
        self.assertEqual(self.factory_naan.run_factory("batter", "water"), "unknown")
