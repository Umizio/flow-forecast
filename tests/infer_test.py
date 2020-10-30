import unittest
from flood_forecast.deployment.infer import load_model
import os
import json


class InferenceTests(unittest.TestCase):

    def setUp(self):
        with open(os.path.join(os.path.dirname(__file__), "test_file.json")) as f:
            self.test_config = json.load(f)
        self.file_path = "gs://task_ts_data/Massachusetts_Middlesex_County.csv"

    def test_load_model(self):
        load_model(self.test_config, self.file_path)


if __name__ == '__main__':
    unittest.main()