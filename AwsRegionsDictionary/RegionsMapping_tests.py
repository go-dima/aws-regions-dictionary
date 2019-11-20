import unittest
from AwsRegionsDictionary.RegionsMapping import findRegion

class AwsRegionDictTests(unittest.TestCase):
    def test_findRegion_regionKeyLower_findKey(self):
        foundRegion = findRegion('eu-central-1')
        self.assertEqual(foundRegion, 'eu-central-1')

    def test_findRegion_regionKeyUpper_findKey(self):
        foundRegion = findRegion('EU-central-1')
        self.assertEqual(foundRegion, 'eu-central-1')

    def test_findRegion_regionNameUpper_findKey(self):
        foundRegion = findRegion('Frankfurt')
        self.assertEqual(foundRegion, 'eu-central-1')

    def test_findRegion_regionNameLower_findKey(self):
        foundRegion = findRegion('frankfurt')
        self.assertEqual(foundRegion, 'eu-central-1')

    def test_findRegion_unknownRegion_excention(self):
        self.assertRaises(KeyError, findRegion, 'Mars')

# Run: python -m unittest discover -s AwsRegionsDictionary -p "*_tests.py"
