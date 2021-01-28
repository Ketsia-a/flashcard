from django.test import TestCase
from .models import Card,Profile,Subject
import datetime as dt
# Create your tests here.

class CardTestClass(TestCase):
    def setUp(self):
        self.kate= Card(title='admcd',note='ndakcjdnkjdcnkjdscnksdjcnsjcnsjcksckdncksndsjncjdn',date ='2021-11-22',image='a.jpg',user = 'Profile.user')

    def test_instance(self):
        self.assertTrue(isinstance(self.kate,Card))    

    def test_save_method(self):
        self.kate.save_card()
        cards = Card.objects.all()
        self.assertTrue(len(cards) > 0)  

    def test_delete_method(self):
        self.kate.save_card()
        self.kate=Card(title='admcd',note='ndakcjdnkjdcnkjdscnksdjcnsjcnsjcksckdncksndsjncjdn',date ='2021-11-22',image='a.jpg',user = 'Profile.user')
        self.kate.save_card()
        self.kate.delete_card()
        deleted = Card.objects.all()
        self.assertEqual(len(deleted),1)      

class SubjectTestClass(TestCase):
    def setUp(self):
        self.cats= Subject(name = 'food')

    def test_instance(self):
        self.assertTrue(isinstance(self.cats,Subject))

    def test_save_method(self):
        self.cats.save_subject() 
        subjects = Subject.objects.all()  
        self.assertTrue(len(subjects) > 0) 