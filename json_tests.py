import unittest
import json
import datetime
import jwt
from Json_Parser import decode_jwt
import db_inserter as db_access

class Test_Methods(unittest.TestCase):
    def test_something(self):
        now = datetime.datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        payload = {"lat": 111.1,
        "long": 112.1,
        "flrID": 1,
        "bldID": 0,
        "dateTime": dt_string,
        "wifiName": "daniel",
        "dwnldSpd": 10,
        "upldSpd": 10,
        "outage": False
        }
        encoded_jwt = jwt.encode(payload, "secret", algorithm="HS256")
        f = open("mock.json", "w")
        f.write(encoded_jwt)
        f.close()
        decoded_jwt = decode_jwt("mock.json")

        assert (decoded_jwt == payload) is True
    def test_db(self):
        db_access.write_into_db("mock.json")

if __name__ == '__main__':
    unittest.main()





# add assertion here


if __name__ == '__main__':
    unittest.main()
