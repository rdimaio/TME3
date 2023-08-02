import unittest
import tempfile
import os
import json
from json_graph_extractor.json_graph_extractor import JsonGraphExtractor

SAMPLE_DATA_DICT = {
    "pkg1": ["pkg2", "pkg3"],
    "pkg2": ["pkg3"],
    "pkg3": []
}


EXPECTED_PKG1_OUTPUT = "- pkg1\n - pkg2\n  - pkg3\n - pkg3\n"
EXPECTED_PKG2_OUTPUT = "- pkg2\n - pkg3\n"
EXPECTED_PKG3_OUTPUT = "- pkg3\n"

class TestJsonGraphExtractor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.temp_json_file = tempfile.NamedTemporaryFile(mode="w+", delete=True)
        json.dump(SAMPLE_DATA_DICT, cls.temp_json_file)
        cls.temp_json_file.flush()
        cls.jge = JsonGraphExtractor(cls.temp_json_file.name)

    @classmethod
    def tearDownClass(cls):
        cls.temp_json_file.close()

    def test_json_to_dict(self):
        actual_output = self.jge.json_to_dict()
        self.assertEqual(actual_output, SAMPLE_DATA_DICT)

    def test_get_key_and_values(self):
        actual_pkg1_output = self.jge._get_key_and_values("pkg1", 0)
        actual_pkg2_output = self.jge._get_key_and_values("pkg2", 0)
        actual_pkg3_output = self.jge._get_key_and_values("pkg3", 0)

        self.assertEqual(actual_pkg1_output, EXPECTED_PKG1_OUTPUT)
        self.assertEqual(actual_pkg2_output, EXPECTED_PKG2_OUTPUT)
        self.assertEqual(actual_pkg3_output, EXPECTED_PKG3_OUTPUT)

    def test_dict_to_graph(self):
        expected_output = EXPECTED_PKG1_OUTPUT + EXPECTED_PKG2_OUTPUT + EXPECTED_PKG3_OUTPUT
        actual_output = self.jge.dict_to_graph()
        self.assertEqual(actual_output, expected_output)

if __name__ == '__main__':
    unittest.main()