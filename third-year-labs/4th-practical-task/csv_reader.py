import csv
import requests
from io import StringIO


class CsvReader():
    def read_data(self, path):
        response = requests.get(path)
        response_text = StringIO(response.content.decode('utf-8-sig'))
        reader = csv.DictReader(response_text, delimiter=',')
        return list(reader)
