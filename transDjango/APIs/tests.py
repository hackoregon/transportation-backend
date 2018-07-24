from django.test import TestCase, Client
import json


class BasicEndpointsTest(TestCase):
    fixtures = ["APP_FIXTURE"]

    def setUp(self):
        self.c = Client()

    def test_root_get_request_sends_200(self):
        response = self.c.get("/transport/")
        self.assertEqual(response.status_code, 200)
