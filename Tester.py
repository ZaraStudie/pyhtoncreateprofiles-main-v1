import unittest
import csv
import json
import csvtojson
csv_file = 'profiles1.csv'
json_file = 'data.json'

class TestCSVFile(unittest.TestCase):
    
    def test_columns_count(self):
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            header = next(reader)
            self.assertEqual(len(header), 12, "The CSV file does not contain 12 columns")

    def test_rows_count(self):
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            self.assertGreaterEqual(len(rows), 900, "The CSV file does not contain at least 900 rows")

    
class TestJSONFile(unittest.TestCase):

    def test_properties_existence(self):
        with open(json_file, 'r') as file:
            data = json.load(file)
            required_properties = ['Givenname', 'Surname', 'Birthday', 'Country'] 
            for prop in required_properties:
                self.assertIn(prop, data[0], f"The JSON file does not contain property: {prop}")

    def test_rows_count(self):
        with open(json_file, 'r') as file:
            data = json.load(file)
            self.assertGreaterEqual(len(data), 900, "The JSON file does not contain at least 900 rows")

class TestCSVToJSON(unittest.TestCase):

    def test_conversion(self):
        csvtojson.convert_csv_to_json(csv_file,json_file)
        with open(json_file, 'r') as file:
            generated_data = json.load(file)
        with open(json_file, 'r') as file:
            expected_data = json.load(file)

        self.assertEqual(generated_data, expected_data, "The generated JSON does not match the expected JSON")

if __name__ == '__main__':
    unittest.main()
