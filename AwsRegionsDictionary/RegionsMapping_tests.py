import unittest
from RegionsMapping import findRegion

class AwsRegionDictTests(unittest.TestCase):
    def test_findregion_by_key(self):
        foundRegion = findRegion('eu-central-1')
        self.assertEqual(foundRegion, 'eu-central-1')

    def test_findRegion_by_name(self):
        foundRegion = findRegion('Frankfurt')
        self.assertEqual(foundRegion, 'eu-central-1')

    def test_findRegion_unknown_region(self):
        self.assertRaises(KeyError, findRegion, 'Mars')

# Run: python -m unittest discover -s AwsRegionsDictionary -p "*_tests.py"
