import unittest
import copy
from avi.heat.avi_utils import cmp_a_in_b
from avi.heat.avi_utils import replace_refs_with_uuids


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

    def check_replace_refs_with_uuids(self, obj):
        print "Before: %s" % obj
        replace_refs_with_uuids(obj)
        print "After: %s" % obj
        self.assertTrue("ref" not in str(obj))
        self.assertTrue("uuid" in str(obj))

    def test_replace_refs_with_uuids(self):
        obj = {"single_ref": "http://blah.com/api/vs/vs-21323#vsname",
               "single_short_ref": "/vs/vs-2322",
               "multi_refs": ["/vs/vs-23241", "se/se-23412412#dfjha"]
               }
        self.check_replace_refs_with_uuids(copy.deepcopy(obj))

        obj1 = {"k1": copy.deepcopy(obj), "k2": None}
        self.check_replace_refs_with_uuids(obj1)

        obj2 = {"k2": [copy.deepcopy(obj), copy.deepcopy(obj)]}
        self.check_replace_refs_with_uuids(obj2)

