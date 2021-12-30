import requests
import json
from psycopg2.extras import Json

class Utility:

    @staticmethod
    def request(url):
        r = requests.get(url)
        return r.json()

    @staticmethod
    def save(data, filepath):
        with open(filepath, 'w') as file:
            json.dump(data, file)

    @staticmethod
    def generate_columns(data):
        return [list(x.keys()) for x in data][0]

    @staticmethod
    def generate_all_values(data):
        values = [list(x.values()) for x in data]
        values_str = ""

        for i, record in enumerate(values):
            # declare empty list for values
            val_list = []

            # append each value to a new list of values
            for v, val in enumerate(record):
                if type(val) == str:
                    val = str(Json(val)).replace('"', '')
                val_list += [str(val)]

            # put parenthesis around each record string
            values_str += "(" + ', '.join(val_list) + "),\n"

        # remove the last comma and end SQL with a semicolon
        values_str = values_str[:-2] + ";"

        return  values_str
