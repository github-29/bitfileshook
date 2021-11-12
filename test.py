import unittest
from bitFileView import app

class test_app(unittest.TestCase):

    def test_happy_path(self):
        data = {
            "username": "sushil29",
            "password": "Sush@2907",
            # "branch": "master"
        }
        tester = app.test_client()
        response = tester.post('/bitapi', data=data)
        self.assertEqual(200, response.status_code)

    # def test_invalid_username(self):
    #     data = {
    #         "username": "sushil293",
    #         "password": "Sush@2907",
    #         # "branch": "master"
    #     }
    #     tester = app.test_client()
    #     response = tester.post('/bitapi/', data=data)
    #     self.assertEqual(401, response.status_code)
    #
    # def test_invalid_password(self):
    #     data = {
    #         "username": "sushil29",
    #         "password": "Sush@29078",
    #         # "branch": "master"
    #     }
    #     tester = app.test_client()
    #     response = tester.post('/bitapi/', data=data)
    #     self.assertEqual(401, response.status_code)

    # def test_invalid_branch(self):
    #     data = {
    #         "username": "sushil29",
    #         "password": "Sush@2907",
    #         "branch": "testmaster"
    #     }
    #     tester = app.test_client()
    #     response = tester.post('/api/bit/', data=data)
    #     self.assertEqual(404, response.status_code)
