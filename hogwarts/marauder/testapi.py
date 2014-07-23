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
        all_characters = Character.objects.all()
        url = reverse('characters_api')
        response = self.fetch_url(url)
        expected = [{'quote_by': 'Albus Dumbledore', 'id': 1, 'wand': '15 inch elder wood with thestral hair', 'quote': "Why doesn't anyone ever give me warm socks?", 'description': 'Albus Dumbledore was the only wizard Voldemort was wary of.', 'name': 'Albus Dumbledore', 'magical': True}, {'quote_by': 'neville on the battlefield', 'id': 24, 'wand': 'a very good wand', 'magical': True, 'quote': 'Die, basilisk!', 'description': 'Neville became a surprisingly attractive teenager.', 'name': 'Neville Longbottom'}]
        self.assertEqual(response, expected)


class TestPotionAPI(TestCase):

    @classmethod
    def setUpClass(self):
        p = Potion.objects.create(
            id=1,
            name='AmortentiaTest',
            difficulty='Advanced',
            physical_description='Steam rises from Amortentia in coil-like designs.',
            effects='Amortentia is the most powerful of the love potions.',
            recipe='The ingredients are 7 rose thorns...',
            notable_uses='Department of Mysteries'
        )
        p2 = Potion.objects.create(
            id=24,
            name='VeritaserumTest',
            difficulty='Advanced',
            physical_description='No color and no odor.',
            effects='You have to tell the truth.',
            recipe='Unknown',
            notable_uses='Umbridge'
        )

    def fetch_url(self, url):
        client = Client()
        response = client.get(url)
        return json.loads(response.content.decode("utf-8"))


    def testDetail(self):
        p = Potion.objects.all()[0]
        url = reverse('potions_api', kwargs={'id': p.id})
        response = self.fetch_url(url)
        expected = {
            "id": p.id, 
            "name": p.name, 
            "difficulty": p.wand if p.wand else None,
            "physical_description": p.description,
            "effects": p.magical,
            "recipe": p.quote if p.quote else None,
            "notable_uses": p.quote_by if p.quote_by else None
        }
        self.assertEqual(response, expected)

    def testIndex(self):
        all_potions = Potions.objects.all()
        url = reverse('potions_api')
        response = self.fetch_url(url)
        expected = [{'id':1, 'name': 'AmortentiaTest', 'difficulty':'Advanced', 'physical_description':'Steam rises from Amortentia in coil-like designs', 'effects':'Amortentia is the most powerful of the love potions', 'recipe':'The ingredients are 7 rose thorns...', 'notable_uses':'Department of Mysteries'}, {'id':24, 'name':'VeritaserumTest', 'difficulty':'Advanced', 'physical_description':'No color and no odor.', 'effects':'You have to tell the truth.', 'recipe':'Unknown', 'notable_uses':'Umbridge'}]
        self.assertEqual(response, expected)
