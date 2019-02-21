from django.test import TestCase, Client
from django.urls import reverse
from stockapp.models import Stock, User
from django.core.exceptions import ObjectDoesNotExist


class GetOrderDetailsTestCase(TestCase):
    # setUp method is called before each test in this class
    def setUp(self):
        newUser = User(username='Joe', password='bread', balance=float(1500))
        newUser.save()
        pass  # nothing to set up

    def test_creation(self):
        try:
            user = User.objects.get(username='Joe')
            self.assertEquals(user.password, 'bread')
        except ObjectDoesNotExist:
            self.fail('Error')

    def test_read(self):
        user = User.objects.get(username='Joe')
        self.assertEquals(user.password, 'bread')

    def test_update(self):
        user = User.objects.get(username='Joe')
        user.password = 'dog'
        self.assertEquals(user.password, 'dog')

    def test_delete(self):
        user = User.objects.get(username='Joe')
        user.delete()
        try:
            retrieval = User.objects.get(username='Joe')
            pass
        except ObjectDoesNotExist:
            self.fail('Error')

    # tearDown method is called after each test

    def tearDown(self):
        pass  # nothing to tear down
