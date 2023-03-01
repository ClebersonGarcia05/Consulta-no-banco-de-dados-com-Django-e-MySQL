from django.test import TestCase
from model_mommy import mommy


class UserTestCase(TestCase):
    def setUp(self):
        self.user = mommy.make('core.User')

    def test_str(self):
        self.assertEquals(str(self.user), self.user.name)

class OrderTestCase(TestCase):
    def setUp(self):
        self.item = mommy.make('Order')

    def test_str(self):
        self.assertEquals(str(self.item), self.item.item)
    