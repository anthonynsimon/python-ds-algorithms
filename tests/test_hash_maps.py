import unittest
from lib.data_structures.hash_map_simple import HashMapSimple
from lib.data_structures.hash_map import HashMap


class TesthashMaps(unittest.TestCase):

    def testHashMapSimple(self):
        hash_map = HashMapSimple()
        hash_map.put("radar", 1554)
        hash_map.put(15, "John")
        hash_map.put("radar", 768)

        self.assertEqual(hash_map.get("radar"), 768)
        self.assertEqual(hash_map.get("raard"), False)
        self.assertEqual(hash_map.get("John"), False)
        self.assertEqual(hash_map.get(15), "John")

        hash_map.put("New York", "NY")
        hash_map.put("Michigan", "MI")
        hash_map.put("California", "CA")
        hash_map.put("Indiana", "IN")

        self.assertEqual(hash_map.get("Michigan"), "MI")
        self.assertEqual(hash_map.get("NY"), False)

    def testHashMapAlternate(self):
        hash_map = HashMap()

        hash_map.remove("New York")
        self.assertFalse(hash_map.get("New York"))

        hash_map.put("radar", 1554)
        hash_map.put(129, "John")
        hash_map.put("radar", 768)
        hash_map.put("a", 882)

        for i in range(128):
            hash_map.put(i, "TRASH VALUE")
        for i in range(128):
            hash_map.remove(i)

        self.assertEqual(hash_map.get("a"), 882)
        self.assertEqual(hash_map.get("radar"), 768)
        self.assertEqual(hash_map.get("raard"), False)
        self.assertEqual(hash_map.get("John"), False)
        self.assertEqual(hash_map.get(129), "John")

        hash_map.put("New York", "NY")
        hash_map.put("Michigan", "MI")
        hash_map.put("California", "CA")
        hash_map.put("Indiana", "IN")

        hash_map.remove("New York")

        self.assertEqual(hash_map.get("Michigan"), "MI")
        self.assertFalse(hash_map.get("NY"))
        self.assertFalse(hash_map.get("New York"))