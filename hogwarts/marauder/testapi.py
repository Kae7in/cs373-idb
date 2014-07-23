#!/usr/bin/env python3
from django.test import TestCase, TransactionTestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from marauder.models import *
import json

class TestCharacterAPI(TransactionTestCase):

    def setUp(self):
        c = Character.objects.create(
            id=1,
            name='Albus Dumbledore',
            wand='15 inch elder wood with thestral hair',
            description=('Albus Dumbledore was the only wizard '
                        'Voldemort was wary of.'),
            magical=True,
            quote="Why doesn't anyone ever give me warm socks?",
            quote_by='Albus Dumbledore',
            sex='M'
        )
        d = Character.objects.create(
            id=24,
            name='Neville Longbottom',
            wand='a very good wand',
            description=('Neville became a surprisingly attractive teenager.'),
            magical=True,
            quote="Die, basilisk!",
            quote_by='neville on the battlefield',
            sex='M',

        )

    def fetch_url(self, url):
        client = Client()
        response = client.get(url)
        return json.loads(response.content.decode("utf-8"))


    def testDetail(self):
        c = Character.objects.all()[0]
        url = reverse('character_api', kwargs={'id': c.id})
        response = self.fetch_url(url)
        expected = {
            "id": c.id, 
            "name": c.name, 
            "wand": c.wand if c.wand else None,
            "description": c.description,
            "magical": c.magical,
            "quote": c.quote if c.quote else None,
            "quote_by": c.quote_by if c.quote_by else None
        }
        self.assertEqual(response, expected)

    def testIndex(self):
        self.maxDiff = None
        all = Character.objects.all()
        url = reverse('characters_api')
        response = self.fetch_url(url)
        expected = [{'quote_by': 'Albus Dumbledore', 'id': 1, 'wand': '15 inch elder wood with thestral hair', 'quote': "Why doesn't anyone ever give me warm socks?", 'description': 'Albus Dumbledore was the only wizard Voldemort was wary of.', 'name': 'Albus Dumbledore', 'magical': True}, {'quote_by': 'neville on the battlefield', 'id': 24, 'wand': 'a very good wand', 'magical': True, 'quote': 'Die, basilisk!', 'description': 'Neville became a surprisingly attractive teenager.', 'name': 'Neville Longbottom'}]
        self.assertEqual(response, expected)

class TestArtifactAPI(TransactionTestCase):

    def setUp(self):
        owner1 = Character.objects.create(
            id=3,
            name='George Weasley',
            wand='good one',
            description='funny',
            magical=True,
            sex='M',
            quote='yes',
            quote_by='yesyes',
        )
        owner2 = Character.objects.create(
            id=5,
            name='stuff with null in it',
            wand='',
            description='kind of funny',
            magical=False,
            sex='F',
            quote='no',
            quote_by='nono',
        )

        a = Artifact.objects.create(
            id=1,
            name='Sword of Griffyndor',
            description='this is a mighty sword',
            kind='asdfasdf',
        )
        a.owners.add(owner1)
        a.owners.add(owner2)
        a.save()

        b = Artifact.objects.create(
            id=3,
            name='Elder Wand',
            description="I can't believe he unearthed Dumbledore's tomb. Rude.",
            kind='some wand thing',
        )


    def fetch_url(self, url):
        client = Client()
        response = client.get(url)
        return json.loads(response.content.decode("utf-8"))


    def testDetail(self):
        a = Artifact.objects.all()[0]
        url = reverse('artifact_api', kwargs={'id': a.id})
        response = self.fetch_url(url)
        expected = {'owners': [3, 5], 'description': 'this is a mighty sword', 'id': 1, 'shop': None, 'kind': 'asdfasdf', 'name': 'Sword of Griffyndor'}
        self.assertEqual(response, expected)

    def testIndex(self):
        all = Artifact.objects.all()
        url = reverse('artifacts_api')
        response = self.fetch_url(url)
        expected = [{'shop': None, 'kind': 'asdfasdf', 'name': 'Sword of Griffyndor', 'description': 'this is a mighty sword', 'owners': [3, 5], 'id': 1}, {'shop': None, 'kind': 'some wand thing', 'name': 'Elder Wand', 'description': "I can't believe he unearthed Dumbledore's tomb. Rude.", 'owners': [], 'id': 3}]
        self.assertEqual(response, expected)
