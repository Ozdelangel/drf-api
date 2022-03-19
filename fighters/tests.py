from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Fighters

class FighterTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser', password='pass')
        testuser1.save()

        test_fighter = Fighters.objects.create(name='jon jones', owner=testuser1,description='eye poker')
        test_fighter.save()

    def test_things_model(self):
        fighter = Fighters.objects.get(id=1)
        actual_owner = str(fighter.owner)
        actual_name = str(fighter.name)
        actual_description = str(fighter.description)
        self.assertEqual(actual_owner,'testuser')
        self.assertEqual(actual_name, 'jon jones')
        self.assertEqual(actual_description,'eye poker')