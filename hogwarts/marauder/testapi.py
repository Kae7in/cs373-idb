#!/usr/bin/env python3
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from marauder.models import *
import json

class TestCharacterAPI(TestCase):

    @classmethod
    def setUpClass(self):
        c = Character.objects.create(
            id=1,
            name='Albus Dumbledore',
            wand='15 inch elder wood with thestral hair',
            description=('Albus Dumbledore was the only wizard '
                        'Voldemort was wary of.'),
            magical=True,
            quote="Why doesn't anyone ever give me warm socks?",
            quote_by='Albus Dumbledore'
        )
        d = Character.objects.create(
            id=24,
            name='Neville Longbottom',
            wand='a very good wand',
            description=('Neville became a surprisingly attractive teenager.'),
            magical=True,
            quote="Die, basilisk!",
            quote_by='neville on the battlefield'
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
        all = Character.objects.all()
        url = reverse('characters_api')
        response = self.fetch_url(url)
        expected = [{'quote_by': 'Albus Dumbledore', 'id': 1, 'wand': '15 inch elder wood with thestral hair', 'quote': "Why doesn't anyone ever give me warm socks?", 'description': 'Albus Dumbledore was the only wizard Voldemort was wary of.', 'name': 'Albus Dumbledore', 'magical': True}, {'quote_by': 'neville on the battlefield', 'id': 24, 'wand': 'a very good wand', 'magical': True, 'quote': 'Die, basilisk!', 'description': 'Neville became a surprisingly attractive teenager.', 'name': 'Neville Longbottom'}]
        self.assertEqual(response, expected)
