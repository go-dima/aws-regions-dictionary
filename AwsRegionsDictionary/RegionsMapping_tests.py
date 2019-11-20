import unittest
from AwsRegionsDictionary.RegionsMapping import mapToRegionKey

class AwsRegionDictTests(unittest.TestCase):
    def test_mapToRegionKey_regionKeyLower_findKey(self):
        foundRegion = mapToRegionKey('eu-central-1')
        self.assertEqual(foundRegion, 'eu-central-1')

    def test_mapToRegionKey_regionKeyUpper_findKey(self):
        foundRegion = mapToRegionKey('EU-central-1')
        self.assertEqual(foundRegion, 'eu-central-1')

    def test_mapToRegionKey_regionNameUpper_findKey(self):
        foundRegion = mapToRegionKey('Frankfurt')
        self.assertEqual(foundRegion, 'eu-central-1')

    def test_mapToRegionKey_regionNameLower_findKey(self):
        foundRegion = mapToRegionKey('frankfurt')
        self.assertEqual(foundRegion, 'eu-central-1')

    def test_mapToRegionKey_unknownRegion_excention(self):
        self.assertRaises(KeyError, mapToRegionKey, 'Mars')

# Run: python -m unittest discover -s AwsRegionsDictionary -p "*_tests.py"
