from python_action.unit_test.flask_base_test import BaseTestCase


class cumstor_test(BaseTestCase):

    def test_404_case(self):
        response = self.get_url_base(url='http://www.baidu.com')
        assert 200 == response.status_code
        self.assertIsNotNone(response.status_code)
