from unittest import TestCase
import requests
import time


class BaseTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def get_url_base(self, url, header=None, data=None):
        result = ""
        try:
            result = requests.get(url)
        except Exception as ex:
            print("error:{}".format(ex))
        return result
