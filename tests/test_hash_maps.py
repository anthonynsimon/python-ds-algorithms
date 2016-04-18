import unittest
from DataStructures import HashMapSimple
from DataStructures import HashMapAlternate


class TesthashMaps(unittest.TestCase):

    def testHashMapSimple(self):
        hashMap = HashMapSimple.HashMapSimple()
        hashMap.put("radar", 1554)
        hashMap.put(15, "John")
        hashMap.put("radar", 768)

        self.assertEqual(hashMap.get("radar"), 768)
        self.assertEqual(hashMap.get("raard"), False)
        self.assertEqual(hashMap.get("John"), False)
        self.assertEqual(hashMap.get(15), "John")

        hashMap.put("New York", "NY")
        hashMap.put("Michigan", "MI")
        hashMap.put("California", "CA")
        hashMap.put("Indiana", "IN")

        self.assertEqual(hashMap.get("Michigan"), "MI")
        self.assertEqual(hashMap.get("NY"), False)

    def testHashMapAlternate(self):
        hashMap = HashMapAlternate.HashMapAlternate()

        hashMap.remove("New York")
        self.assertFalse(hashMap.get("New York"))

        hashMap.put("radar", 1554)
        hashMap.put(129, "John")
        hashMap.put("radar", 768)
        hashMap.put("a", 882)

        for i in range(128):
            hashMap.put(i, "TRASH VALUE")
        for i in range(128):
            hashMap.remove(i)

        self.assertEqual(hashMap.get("a"), 882)
        self.assertEqual(hashMap.get("radar"), 768)
        self.assertEqual(hashMap.get("raard"), False)
        self.assertEqual(hashMap.get("John"), False)
        self.assertEqual(hashMap.get(129), "John")

        hashMap.put("New York", "NY")
        hashMap.put("Michigan", "MI")
        hashMap.put("California", "CA")
        hashMap.put("Indiana", "IN")

        hashMap.remove("New York")

        self.assertEqual(hashMap.get("Michigan"), "MI")
        self.assertFalse(hashMap.get("NY"))
        self.assertFalse(hashMap.get("New York"))