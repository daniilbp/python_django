from django.test import SimpleTestCase
from app_logic.helpers import check_access_by_age, working_time, devider, join_str


class BusinessLogicTest(SimpleTestCase):
    def test_access_denied(self):
        self.assertEqual(check_access_by_age(18), True)

    def test_access_denied_2(self):
        self.assertTrue(working_time(8))

    def test_access_denied_3(self):
        self.assertFalse(devider(2, 0))

    def test_access_denied_4(self):
        self.assertEqual(join_str(['abc def'], '123 456'), False)
