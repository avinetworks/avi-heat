import unittest
from avi.heat.avi_utils import cmp_a_in_b


class TestAviResource(unittest.TestCase):
    def test_cmp_function(self):
        self.assertTrue(cmp_a_in_b("a", "a"))
        self.assertTrue(cmp_a_in_b(3, 3))

        a = ["A"]
        b = ["B", "A"]
        self.assertTrue(cmp_a_in_b(a, b))

        a = ["A", "B"]
        b = ["C", "B", "A"]
        self.assertTrue(cmp_a_in_b(a, b))

        a = ["A", "B", "D"]
        b = ["C", "B", "A"]
        self.assertFalse(cmp_a_in_b(a, b))

        a = {"A": "A"}
        b = {"B": "B", "A": "A"}
        self.assertTrue(cmp_a_in_b(a, b))

        a["B"] = "B"
        self.assertTrue(cmp_a_in_b(a, b))

        a["C"] = "C"
        self.assertFalse(cmp_a_in_b(a, b))
