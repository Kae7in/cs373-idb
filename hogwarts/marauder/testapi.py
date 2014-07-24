#!/usr/bin/env python3
from django.test import TestCase, TransactionTestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from marauder.models import *
import json

def fetch_url(url):
    client = Client()
    response = client.get(url)
    return json.loads(response.content.decode("utf-8"))

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

    def testDetail(self):
        c = Character.objects.all()[0]
        url = reverse('character_api', kwargs={'id': c.id})
        response = fetch_url(url)
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
        self.maxDiff = None
        url = reverse('characters_api')
        response = fetch_url(url)
        expected = [{'quote_by': 'Albus Dumbledore', 'id': 1, 'wand': '15 inch elder wood with thestral hair', 'quote': "Why doesn't anyone ever give me warm socks?", 'description': 'Albus Dumbledore was the only wizard Voldemort was wary of.', 'name': 'Albus Dumbledore', 'magical': True}, {'quote_by': 'neville on the battlefield', 'id': 24, 'wand': 'a very good wand', 'magical': True, 'quote': 'Die, basilisk!', 'description': 'Neville became a surprisingly attractive teenager.', 'name': 'Neville Longbottom'}]
        self.assertEqual(response, expected)


class TestPotionAPI(TransactionTestCase):

    def setUp(self):
        p = Potion.objects.create(
            id=1,
            title='AmortentiaTest',
            difficulty='A',
            physical_description='Steam rises from Amortentia in coil-like designs.',
            effects='Amortentia is the most powerful of the love potions.',
            recipe='The ingredients are 7 rose thorns...',
            notable_uses='Department of Mysteries'
        )
        p2 = Potion.objects.create(
            id=24,
            title='VeritaserumTest',
            difficulty='A',
            physical_description='No color and no odor.',
            effects='You have to tell the truth.',
            recipe='Unknown',
            notable_uses='Umbridge'
        )
        p.save()
        p2.save()

    def testDetail(self):
        p = Potion.objects.all()[0]
        assert len(Potion.objects.all()) == 2
        url = reverse('potion_api', kwargs={'id': p.id})
        response = fetch_url(url)
        expected = {
            "id": p.id, 
            "title": p.title, 
            "difficulty": p.difficulty,
            "physical_description": p.physical_description,
            "effects": p.effects,
            "recipe": p.recipe,
            "notable_uses": p.notable_uses
        }
        self.assertEqual(response, expected)

    def testIndex(self):
        self.maxDiff=None
        all_potions = Potion.objects.all()
        assert len(all_potions) != 0
        url = reverse('potions_api')
        response = fetch_url(url)
        expected = [{'id':1, 'title': 'AmortentiaTest', 'difficulty':'A', 'physical_description':'Steam rises from Amortentia in coil-like designs.', 'effects':'Amortentia is the most powerful of the love potions.', 'recipe':'The ingredients are 7 rose thorns...', 'notable_uses':'Department of Mysteries'}, {'id':24, 'title':'VeritaserumTest', 'difficulty':'A', 'physical_description':'No color and no odor.', 'effects':'You have to tell the truth.', 'recipe':'Unknown', 'notable_uses':'Umbridge'}]
        self.assertEqual(response, expected)


class TestCreatureAPI(TestCase):

    @classmethod
    def setUpClass(self):
        c = Creature.objects.create(
            id=1,
            name='HippogriffTest',
            description='magnificent',
            classification='Beast',
            rating=3
        )
        c2 = Creature.objects.create(
            id=24,
            name='WerewolfTest',
            description='wolf-men/women-people',
            classification='Beast',
            rating=3
        )

    def testDetail(self):
        c = Creature.objects.all()[0]
        url = reverse('creature_api', kwargs={'id': c.id})
        response = fetch_url(url)
        expected = {
            "id": c.id, 
            "name": c.name, 
            "description": c.description,
            "classification": c.classification,
            "rating": c.rating
        }
        self.assertEqual(response, expected)

    def testIndex(self):
        all_creatures = Creature.objects.all()
        url = reverse('creatures_api')
        response = fetch_url(url)
        expected = [{'id':1, 'name':'HippogriffTest', 'description':'magnificent', 'classification':'Beast', 'rating':3},{'id':24, 'name':'WerewolfTest', 'description':'wolf-men/women-people', 'classification':'Beast', 'rating': 3}]
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
        a = Artifact.objects.all()[0]
        url = reverse('artifact_api', kwargs={'id': a.id})
        response = fetch_url(url)
        expected = {'owners': [3, 5], 'description': 'this is a mighty sword', 'id': 1, 'shop': None, 'kind': 'asdfasdf', 'name': 'Sword of Griffyndor'}
        self.assertEqual(response, expected)

    def testIndex(self):
        all = Artifact.objects.all()
        url = reverse('artifacts_api')
        response = fetch_url(url)
        expected = [{'shop': None, 'kind': 'asdfasdf', 'name': 'Sword of Griffyndor', 'description': 'this is a mighty sword', 'owners': [3, 5], 'id': 1}, {'shop': None, 'kind': 'some wand thing', 'name': 'Elder Wand', 'description': "I can't believe he unearthed Dumbledore's tomb. Rude.", 'owners': [], 'id': 3}]
        self.assertEqual(response, expected)
