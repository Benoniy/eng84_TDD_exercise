import unittest
import naan_factory


class naanTest(unittest.TestCase):

    def test_make_dough(self):
        self.assertEqual(naan_factory.make_dough("flour", "water"), "dough")


    def test_bake_dough(self):
        self.assertEqual(naan_factory.bake_dough("dough"), "naan bread")

    def test_run_factory(self):
        self.assertEqual(naan_factory.run_factory("flour", "water"), "naan bread")

