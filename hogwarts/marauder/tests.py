from django.test import TestCase
import marauder.models as lm
from datetime import date
from django.test.utils import override_settings
from django.core.management import call_command
import haystack
from haystack.query import SearchQuerySet, AutoQuery
from marauder.views import MySearchView, generateSearchQuery
import os

"""
  MODEL TESTS
"""
class CharacterTest(TestCase):
    def test_squib_character(self):
        argus = lm.Character()
        argus.name = 'Argus Filch'
        argus.magical = False
        argus.save()

        dad = lm.Character()
        dad.magical = True
        dad.save()

        mom = lm.Character()
        mom.magical = True
        mom.save()

        r1 = lm.Relationship()
        r1.character1 = argus
        r1.descriptor1 = 'Son'
        r1.character2 = dad
        r1.descriptor2 = 'Father'
        r1.save()

        r2 = lm.Relationship()
        r2.character1 = mom
        r2.descriptor1 = 'Mother'
        r2.character2 = argus
        r2.descriptor2 = 'Son'
        r2.save()

        self.assertTrue(argus.is_squib())

    def test_harry_character(self):
        harry = lm.Character()
        harry.name = 'Harry Potter'
        harry.magical = True
        harry.birthday = "7/31/1980"
        harry.save()

        snape = lm.Character()
        snape.magical = True
        snape.save()

        r1 = lm.Relationship()
        r1.character1 = harry
        r1.descriptor1 = 'student'
        r1.character2 = snape
        r1.descriptor2 = 'professor'
        r1.save()

        self.assertFalse(harry.is_squib())
        self.assertEqual(harry.birthday, "7/31/1980")
        self.assertTrue(harry.magical)

    def test_malfoy_character(self):
        malfoy = lm.Character()
        malfoy.name = 'Draco Malfoy'
        malfoy.magical = True
        malfoy.birthday = "6/5/1980"
        malfoy.save()

        dad = lm.Character()
        dad.magical = True
        dad.save()

        r1 = lm.Relationship()
        r1.character1 = malfoy
        r1.descriptor1 = 'son'
        r1.character2 = dad
        r1.descriptor2 = 'father'
        r1.save()

        self.assertFalse(malfoy.is_squib())
        self.assertEqual(malfoy.birthday, "6/5/1980")
        self.assertTrue(malfoy.magical)

class CreatureTest(TestCase):
    def setUp(self):
        creature = lm.Creature()
        creature.name = 'Goblin'
        creature.description = "Goblins are mysterious and good with money.\n"
        creature.classification = 'Being'
        creature.rating = 3
        creature.save()
    
    def test_create_creature(self):
        all_creatures = lm.Creature.objects.all()
        self.assertEqual(len(all_creatures), 1)
        creature = lm.Creature.objects.first()
        self.assertEqual(creature.name, 'Goblin')
        self.assertEqual(creature.description, 'Goblins are mysterious and good with money.\n')
        self.assertEqual(creature.classification, 'Being')
        self.assertEqual(creature.rating, 3)
        self.assertEqual(creature.get_rating_display(), 'XXX')

    def test_string_creature(self):
        creature = lm.Creature.objects.first()
        self.assertEqual(str(creature), creature.name)

    def test_neutralize_creature(self):
        boggart = lm.Creature()
        boggart.name = 'Boggart'
        boggart.rating = 0
        boggart.save()

        spell = lm.Spell()
        spell.incantation = 'Riddikulus'
        spell.alias = 'Boggart Banishing Spell'
        spell.creature = boggart
        spell.kind = 'Defensive'
        spell.save()

        self.assertTrue(boggart.neutralize('Riddikulus'))
        self.assertFalse(boggart.neutralize('Lumos'))


class ShopTest(TestCase):
    def setUp(self):
        shop = lm.Shop()
        shop.name = "Weasley's Wizard Wheezes"
        shop.description = "A practical magical joke shop run by the Weasley brothers. Well, one brother now..."
        shop.kind = 'shop'
        shop.save()

    def test_create_shop(self):
        shop = lm.Shop.objects.first()
        self.assertEqual(shop.name, "Weasley's Wizard Wheezes")
        self.assertEqual(shop.description, "A practical magical joke shop run by the Weasley brothers. Well, one brother now...")
        self.assertEqual(shop.kind, 'shop')

    def test_shop_with_locations(self):
        shop = lm.Shop.objects.first()
        location = lm.Location()
        location.name = 'Diagon Alley'
        location.save()
        shop.locations.add(location)
        shop.save()

        first_shop = lm.Shop.objects.first()
        self.assertEqual(first_shop.locations.all().first(), location)

    def test_shop_with_owners(self):       
        shop = lm.Shop.objects.first()
        character = lm.Character()
        character.name = 'George Weasley'
        character.shop = shop
        character.save()

        first_shop = lm.Shop.objects.first()
        self.assertEqual(first_shop.owners.first(), character)

    def test_string_shop(self):
        shop = lm.Shop.objects.first()
        self.assertEqual(str(shop), shop.name)

class LocationTest(TestCase):
    def setUp(self):
        location = lm.Location()
        location.name = 'Knockturn Alley'
        location.description = 'Only naughty wizards go here. Why are you here? You must be naughty.'
        location.kind = 'shopping district'
        location.save() 

    def test_create_location(self):
        location = lm.Location.objects.first()
        self.assertEqual(location.name, 'Knockturn Alley')
        self.assertEqual(location.description, 'Only naughty wizards go here. Why are you here? You must be naughty.')
        self.assertEqual(location.kind, 'shopping district')

    def test_string_location(self):
        location = lm.Location.objects.first()
        self.assertEqual(str(location), location.name)

class StoryTest(TestCase):
    def setUp(self):
        story = lm.Story()
        story.name = 'Deathly Hallows'
        story.description = 'There were three brothers and they all died.'
        story.kind = 'legend'
        story.date = date(1200, 1, 1)
        story.save()

    def test_create_story(self):
        story = lm.Story.objects.first()
        self.assertEqual(story.name, 'Deathly Hallows')
        self.assertEqual(story.description, 'There were three brothers and they all died.')
        self.assertEqual(story.kind, 'legend')
        self.assertEqual(story.date.year, 1200)

    def test_story_with_book(self):
        story = lm.Story.objects.first()
        book = lm.Book()
        book.name = 'The Tales of Beedle the Bard'
        book.save()
        story.book = book
        story.save()

        first_story = lm.Story.objects.first()
        self.assertEqual(first_story.book.name, book.name)

    def test_story_with_artifact(self):
        story = lm.Story.objects.first()
        elder_wand = lm.Artifact()
        elder_wand.name = 'Elder Wand'
        elder_wand.save()
        story.artifacts.add(elder_wand)
        story.save()

        first_story = lm.Story.objects.first()
        self.assertEqual(first_story.artifacts.first().name, elder_wand.name)

    def test_story_with_character(self):
        story = lm.Story.objects.first()
        ignotus = lm.Character()
        ignotus.name = 'Ignotus Peverell'
        ignotus.save()
        story.characters.add(ignotus)
        story.save()

        first_story = lm.Story.objects.first()
        self.assertEqual(first_story.characters.first().name, ignotus.name)

    def test_str_story(self):
        story = lm.Story.objects.first()
        self.assertEqual(str(story), story.name)

    def test_century_story(self):
        story = lm.Story.objects.first()
        self.assertEqual(story.century(), 13)

    def test_formatted_date_story(self):
        story = lm.Story.objects.first()
        self.assertEqual(story.formatted_date(), "13th Century")

        story.date = story.date.replace(year = 1981)
        story.save()
        self.assertEqual(story.formatted_date(), 1981)

        story.date = story.date.replace(month = 5)
        story.save()
        self.assertEqual(story.formatted_date(), "May 01, 1981")

class SpellTest(TestCase):
    def setUp(self):
        spell = lm.Spell()
        spell.incantation = 'Expecto Patronum'
        spell.alias = 'Patronus Charm'
        spell.effect = "evokes a positive energy force"
        spell.notable_uses = "Harry used it for dementors."
        spell.unforgivable = False 
        spell.kind = 'Charm'
        spell.difficulty = 'Extremely Diffucult'
        spell.save()
        
    def test_create_spell(self):
        all_spells = lm.Spell.objects.all()
        self.assertEqual(len(all_spells), 1)
        spell = lm.Spell.objects.first()
        self.assertEqual(spell.incantation, 'Expecto Patronum')
        self.assertEqual(spell.alias, 'Patronus Charm')
        self.assertEqual(spell.effect, "evokes a positive energy force")
        self.assertEqual(spell.notable_uses, 'Harry used it for dementors.')
        self.assertEqual(spell.unforgivable, False)
        self.assertEqual(spell.kind, 'Charm')

    def test_relationships_spell(self):
        spell = lm.Spell.objects.first()
        creature = lm.Creature()
        creature.name = 'Dementor'
        creature.classification = 'NB'
        creature.rating = 5
        creature.save()
        spell.creature = creature
        spell.save()

        first_spell = lm.Spell.objects.first()
        self.assertEqual(first_spell.creature, creature)

    def test_string_spell(self):
        spell = lm.Spell.objects.first()
        self.assertEqual(str(spell), spell.incantation)

class PotionTest(TestCase):
    def setUp(self):
        
        potion = lm.Potion()
        potion.title = "Felix Felices"
        potion.difficulty = 'A'
        potion.physical_description = "Its color is molten gold..."
        potion.recipe = 'Add to the cauldron an Ashwinder egg and horseradish before heating...'
        potion.effects = "Increases the drinker's luck. Overdose can..."
        potion.notable_uses = "Hermoine, Ginny and Ron used Felix Felices to evade the curses of Death Eaters..."
        potion.save()
    
    def test_create_potion(self):
        potions = lm.Potion.objects.all()
        self.assertEqual(len(potions), 1)
        potion_created = potions.first()
        
        
        self.assertEqual("Felix Felices", potion_created.title)
        self.assertEqual("A", potion_created.difficulty)
        self.assertEqual("Its color is molten gold...", potion_created.physical_description)
        self.assertEqual("Add to the cauldron an Ashwinder egg and horseradish before heating...", potion_created.recipe)
        self.assertEqual("Increases the drinker's luck. Overdose can...", potion_created.effects)
        self.assertEqual("Hermoine, Ginny and Ron used Felix Felices to evade the curses of Death Eaters...", potion_created.notable_uses)
        self.assertEqual("images/empty.jpg", potion_created.image)
        all_ingredients = potion_created.ingredients.all()
        self.assertEqual(len(all_ingredients), 0)

    def test_string_potion(self):
        potion = lm.Potion.objects.all().first()
        self.assertEqual(str(potion), "Felix Felices")

    def test_potion_image(self):
        potion = lm.Potion.objects.all().first()
        potion.image = "images/non_empty.jpg"
        potion.save()

    def test_potion_ingredients(self):
        potion = lm.Potion.objects.first()
        creature = lm.Creature()
        creature.name = 'Hippogriff'
        creature.rating = 3
        creature.save()

        ingredient1 = lm.Ingredient()
        ingredient1.name = 'Hippogriff talon'
        ingredient1.creature = creature
        ingredient1.save()

        ingredient2 = lm.Ingredient()
        ingredient2.name = 'Valerian roots'
        ingredient2.save()

        potion.ingredients.add(ingredient1)
        potion.ingredients.add(ingredient2)
        self.assertTrue(ingredient1 in potion.ingredients.all())
        self.assertTrue(ingredient2 in potion.ingredients.all())

    def test_brew_potion(self):
        potion = lm.Potion()
        potion.name = 'Draught of Living Death'
        potion.save()

        ingredient = lm.Ingredient()
        ingredient.name = 'Asphodel in an infusion of wormwood'
        ingredient.save()
        potion.ingredients.add(ingredient)

        ingredient = lm.Ingredient()
        ingredient.name = 'Valerian roots'
        ingredient.save()
        potion.ingredients.add(ingredient)

        ingredient = lm.Ingredient()
        ingredient.name = 'Sopophorous bean'
        ingredient.save()
        potion.ingredients.add(ingredient)

        potion.save()

        available_ingredients = [
            'Asphodel in an infusion of wormwood',
            'Valerian roots',
            'Sopophorous bean'
            ]
        self.assertEqual(potion.brew(available_ingredients), 'Success')
        available_ingredients.append('Newt egg')
        self.assertEqual(potion.brew(available_ingredients), 'Explosion!')
        available_ingredients = ['Valerian roots', 'Wolfsbane', 'Eye of toad']
        self.assertEqual(potion.brew(available_ingredients), 'Failure')

class SchoolTest(TestCase):
    def setUp(self):
        school = lm.School()
        name = "Durmstrang Institute"
        school.name = name
        description = "These guys don't really like muggle-borns very much. Except Krum I guess."
        school.description = description
        school.save()
 
        founder = lm.Character()
        founder.name = 'Nerida Vulchanova'
        founder.save()

        school.founders.add(founder)
        school.save()

    def test_create_school(self):
        schools = lm.School.objects.all()
        self.assertEqual(len(schools), 1)
        school_created = schools.first()
        self.assertEqual(school_created, school_created)
        self.assertEqual("Durmstrang Institute", school_created.name)
        self.assertEqual("These guys don't really like muggle-borns very much. Except Krum I guess.", school_created.description)
        self.assertEqual("images/empty.jpg", school_created.image)
        self.assertEqual('Nerida Vulchanova', school_created.founders.all().first().name)

    def test_school_string(self):
        school = lm.School.objects.first()
        self.assertEqual(str(school), "Durmstrang Institute")	
	
    def test_school_image(self):	
        school = lm.School.objects.first()
        school.image = "images/non_empty.jpg"
        school.save()
        self.assertEqual(school.image, "images/non_empty.jpg")

    def test_school_headmaster(self):
        igor = lm.Character()
        igor.name = 'Igor Karkaroff'
        igor.save()

        school = lm.School.objects.first()
        school.headmasters.add(igor)
        school.save()

        self.assertEqual(igor.school_headmastered, school)

    def test_school_professor(self):
        harfang = lm.Character()
        harfang.name = 'Harfang Munter'
        harfang.save()

        school = lm.School.objects.first()
        school.professors.add(harfang)
        school.save()

        self.assertEqual(harfang.school_taught, school)

    def test_school_student(self):
        viktor = lm.Character()
        viktor.name = 'Viktor Krum'
        viktor.save()

        school = lm.School.objects.first()
        school.students.add(viktor)

        self.assertEqual(viktor.school_attended, school)

class HouseTest(TestCase):
    def setUp(self):
        house = lm.House()
        ghost = lm.Character()
        ghost.name = 'Fat Friar'
        ghost.save()

        founder = lm.Character()
        founder.name = 'Helga Hufflepuff'
        founder.save()
		
        house.name = "Hufflepuff"
        house.description = "Nobody wants to be a Hufflepuff."
        house.quote = 'You might belong in Hufflepuff, Where they are just and loyal, Those patient Hufflepuffs are true, And unafraid of toil.'
        house.quote_by = 'Sorting Hat'
        house.colors = 'Yellow and Black'
        house.mascot = 'Badger'
        house.ghost = ghost
        house.founder = founder

        school2 = lm.School()
        school2.name = "Hogwarts"
        school2.description = "The best school ever"
        school2.save()
        house.school = school2
        house.save()
    
    def test_create_house(self):
        houses = lm.House.objects.all()
        self.assertEqual(len(houses), 1)
        house_created = houses.first()
        self.assertEqual(house_created, house_created)
        
        
        self.assertEqual("Hufflepuff", house_created.name)
        self.assertEqual("Nobody wants to be a Hufflepuff.", house_created.description)
        self.assertEqual("images/empty.jpg", house_created.image)

        self.assertEqual(lm.Character.objects.first(), house_created.ghost)
        self.assertEqual('You might belong in Hufflepuff, Where they are just and loyal, Those patient Hufflepuffs are true, And unafraid of toil.', house_created.quote)
        self.assertEqual('Sorting Hat', house_created.quote_by)
        self.assertEqual('Yellow and Black', house_created.colors)
        self.assertEqual('Badger', house_created.mascot)
        self.assertEqual('Helga Hufflepuff', house_created.founder.name)

    def test_house_string(self):
        house = lm.House.objects.first()
        self.assertEqual(str(house), "Hufflepuff")

    def test_house_image(self):
        house = lm.House.objects.first()
        house.image = "images/non_empty.jpg"
        house.save()
        self.assertEqual(house.image, "images/non_empty.jpg")

    def test_student_house(self):
        student = lm.Character()
        student.name = 'Cedric Diggory' # T-T
        hufflepuff = lm.House.objects.first()
        student.house = hufflepuff
        student.save()

        self.assertEqual(student, hufflepuff.members.first())

class ArtifactTest(TestCase):
    def setUp(self):
        artifact  = lm.Artifact()
        wizzy = lm.Character()

        wizzy.name = "Some Wizard"
        wizzy.magical = True
        wizzy.save()

        shop = lm.Shop()
        shop.name = "Weasleys' Wizard Wheezes"
        shop.description = "A practical magical joke shop run by the Weasley brothers. Well, one brother now..."
        shop.save()

        artifact.name = "Pensieve"
        artifact.description = "The Pensieve is an object used to review memories. It has the appearance of a shallow stone basin, into which are carved runes and strange symbols. It is filled with a silvery substance that appears to be a cloud-like liquid/gas; the collected memories of people who have siphoned their recollections into it. Memories can then be viewed from a non-participant, third-person point of view."
        artifact.shop = shop
        artifact.save()
        artifact.owners.add(wizzy)
        artifact.save()

    def test_artifact_create(self):
        artifacts = lm.Artifact.objects.all()
        a = artifacts[0]
        self.assertEqual(len(artifacts), 1)
        self.assertEqual(a.name, "Pensieve")
        self.assertEqual(str(a), "Pensieve")
        self.assertEqual(a.description, "The Pensieve is an object used to review memories. It has the appearance of a shallow stone basin, into which are carved runes and strange symbols. It is filled with a silvery substance that appears to be a cloud-like liquid/gas; the collected memories of people who have siphoned their recollections into it. Memories can then be viewed from a non-participant, third-person point of view.")
        self.assertEqual(a.kind, "")
        self.assertEqual(a.image, "images/empty.jpg")

    def test_artifact_image(self):
        artifacts = lm.Artifact.objects.all()
        a = artifacts[0]
        a.image = "images/dummy-artifact.jpg" # TODO: What does this actually do, an image is more than a file path string right?
        a.save()
        self.assertEqual(a.image, "images/dummy-artifact.jpg")

    def test_artifact_owners(self):
        a = lm.Artifact.objects.first()
        w = lm.Character.objects.first()
        owners = a.owners.all()
        self.assertEqual(owners[0], w)
        # self.assertIs(a.owner, w) # TODO: Why are they different instances?

        # Reverse lookup. 
        artifact = w.artifacts.first()
        self.assertEqual(artifact, a)

    def test_artifact_shop(self):
        a = lm.Artifact.objects.first()
        s = lm.Shop.objects.first()
        self.assertEqual(a.shop, s)
        self.assertEqual(a.shop.name, "Weasleys' Wizard Wheezes")

        # Reverse lookup 
        artifact = s.artifacts.first()
        self.assertEqual(artifact, a)

class BookTest(TestCase):
    def setUp(self):
        beedle = lm.Character()
        beedle.name = "Beedle The Bard"
        beedle.magical = False
        beedle.save()

        tales_of_beedle = lm.Book()
        tales_of_beedle.name = "Tales Of Beedle The Bard"
        tales_of_beedle.description = "A book of stories that are pretty ok"
        tales_of_beedle.author = beedle
        tales_of_beedle.published_date = date(1200, 1, 1)
        tales_of_beedle.publisher = "Bludger's Books" 
        tales_of_beedle.save()

        brothers = lm.Story()
        brothers.name = "The Three Brothers"
        brothers.description = "There were three brothers and they all died."
        brothers.kind = "legend"
        brothers.date = date(1200, 1, 1)
        brothers.book = tales_of_beedle
        brothers.save()

    def test_book_create(self):
        book   = lm.Book.objects.first()
        self.assertEqual(book.name, "Tales Of Beedle The Bard")
        self.assertEqual(book.description, "A book of stories that are pretty ok")
        self.assertEqual(book.published_date, date(1200, 1, 1))
        self.assertEqual(book.publisher, "Bludger's Books")

    def test_book_author(self):
        book   = lm.Book.objects.first()
        author = lm.Character.objects.first()
        self.assertEqual(book.author, author)
        self.assertEqual(author.books_published.first(), book)

    def test_book_subjects(self):
        book   = lm.Book.objects.first()
        author = lm.Character.objects.first()
        beedle = book.author
        book.subjects.add(beedle)
        book.save()
        self.assertEqual(book.subjects.all()[0], beedle)

    def test_book_story(self):
        book   = lm.Book.objects.first()
        story  = lm.Story.objects.first()
        self.assertEqual(story.book, book)
        self.assertEqual(book.story.first(), story)

class IngredientTest(TestCase):
    def setUp(self):
        ingredient = lm.Ingredient()
        ingredient.name = "Hippogriff Talon"
        hippogriff = lm.Creature()
        hippogriff.name = "Hippogriff"
        hippogriff.description = "."
        hippogriff.classification = "Beast"
        hippogriff.rating = "3"
        hippogriff.save()
        ingredient.creature = hippogriff
        ingredient.save()

    def test_ingredient_create(self):
        ing   = lm.Ingredient.objects.first()
        self.assertEqual(ing.name, "Hippogriff Talon")
        self.assertEqual(ing, lm.Ingredient.objects.first())

    def test_ingredient_attributes(self):
        ing = lm.Ingredient.objects.first()
        self.assertEqual(ing.name, "Hippogriff Talon")
        self.assertEqual(ing.creature, lm.Creature.objects.first())


    def test_ingredient_relationship(self):
        ingredient   = lm.Ingredient.objects.first()
        self.assertEqual(ingredient.creature, lm.Creature.objects.first())

class RelationshipTest(TestCase):
    def setUp(self):
        char1 = lm.Character()
        char1.name = "Harry Potter"
        char1.save()
        char2 = lm.Character()
        char2.name = "James Potter" 
        char2.save()
        rel = lm.Relationship()
        rel.character1 = char1
        rel.character2 = char2
        rel.descriptor1 = "Son"
        rel.descriptor2 = "Father"
        rel.save()
        
    def test_create_relationship(self):
        rel = lm.Relationship.objects.first()
        self.assertEqual(rel.character1, lm.Character.objects.first())
        self.assertEqual(rel.character2, lm.Character.objects.all()[1])
        self.assertEqual(rel.descriptor1, "Son")
        self.assertEqual(rel.descriptor2, "Father")
        

    def test_relationships_str(self):
        rel = lm.Relationship.objects.first()
        self.assertEqual(str(rel), "Harry Potter (Son) -- James Potter (Father)")


"""
  REST API TESTS
"""

from django.test import TransactionTestCase
from django.test.client import Client
from django.core.urlresolvers import reverse
from marauder.models import *
from datetime import date
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


class TestCreatureAPI(TransactionTestCase):

    def setUp(self):
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

class TestStoryAPI(TransactionTestCase):

    def setUp(self):
        s1 = Story.objects.create(
            id = 1,
            name = 'Deathly Hallows',
            description = 'Three bros doin shit',
            kind = 'legend',
            date = date(1200, 1, 1),
            quote = 'la la la',
            quote_by = 'someone',
        )
        s2 = Story.objects.create(
            id = 2,
            name = 'Another Story',
            description = 'Riveting',
            date = date(1987, 1, 1),
        )
        c = Character.objects.create(
            id=3,
            name='George Weasley',
            wand='good one',
            description='funny',
            magical=True,
            sex='M',
            quote='yes',
            quote_by='yesyes',
        )
        s2.characters.add(c)
        s2.save()

    def testDetail(self):
        story = Story.objects.get(pk=2)
        url = reverse('story_api', kwargs={'id': 2})
        response = fetch_url(url)
        expected = {
            'date': '1987-01-01', 'name': 'Another Story', 'kind': None, 
            'characters': [3], 'id': 2, 'quote_by': None, 
            'description': 'Riveting', 'artifacts': None, 'quote': None} 
        self.assertEqual(response, expected)

    def testIndex(self):
        url = reverse('stories_api')
        response = fetch_url(url)
        expected = [
            {'artifacts': None, 'characters': None, 'date': '1200-01-01', 
             'description': 'Three bros doin shit', 'id': 1, 'kind': 'legend', 
             'name': 'Deathly Hallows', 'quote': 'la la la', 'quote_by': 'someone'},
            {'artifacts': None, 'characters': [3], 'date': '1987-01-01', 
             'description': 'Riveting', 'id': 2, 'kind': None, 'name': 'Another Story',
             'quote': None, 'quote_by': None}]
        self.assertEqual(response, expected)

class TestSchoolAPI(TransactionTestCase):

    def setUp(self):
        s1 = School.objects.create(
            id = 1,
            name = 'Durmstrang Institute',
            description = 'These guys dont really like muggle-borns very much. Except Krum I guess.',
        )
        s2 = School.objects.create(
            id = 2,
            name = 'Hogwarts',
            description = 'Harry Land',
            kind = 'School',
            country = 'UK'
        )
        c = Character.objects.create(name = 'Some Old Wizard')
        s2.founders.add(c)
        s2.save()

    def testDetail(self):
        school = School.objects.get(pk=2)
        url = reverse('school_api', kwargs={'id': 2})
        response = fetch_url(url)
        expected = {
            'country': 'UK', 'description': 'Harry Land', 'id': 2,
            'kind': 'School', 'name': 'Hogwarts'} 
        self.assertEqual(response, expected)

    def testIndex(self):
        url = reverse('schools_api')
        response = fetch_url(url)
        expected = [
            {'country': None, 'description': 'These guys dont really like muggle-borns very much. Except Krum I guess.',
            'id': 1, 'kind': None, 'name': 'Durmstrang Institute'},
            {'country': 'UK', 'description': 'Harry Land', 'id': 2, 'kind': 'School', 'name': 'Hogwarts'}]
        self.assertEqual(response, expected)

class TestShopAPI(TransactionTestCase):

    def setUp(self):
        s1 = Shop.objects.create(
            id = 1,
            name = 'Shop1',
            description = 'Sells things',
            kind = 'Shop'
        )
        s2 = Shop.objects.create(
            id = 2,
            name = 'Shop2',
            description = 'Sells more things',
            kind = 'Shop'
        )
        c = Character.objects.create(name = 'Some Old Wizard')
        s2.owners.add(c)
        s2.save()

    def testDetail(self):
        school = Shop.objects.get(pk=2)
        url = reverse('shop_api', kwargs={'id': 2})
        response = fetch_url(url)
        expected = { 
            'id': 2,
            'name': 'Shop2',
            'description': 'Sells more things',
            'owners': [1],
            'locations': None
        } 
        self.assertEqual(response, expected)

    def testIndex(self):
        url = reverse('shops_api')
        response = fetch_url(url)
        expected = [{ 
            'id': 1,
            'name': 'Shop1',
            'description': 'Sells things',
            'owners': None,
            'locations': None }, {
            'id': 2,
            'name': 'Shop2',
            'description': 'Sells more things',
            'owners': [1],
            'locations': None }]
        self.assertEqual(response, expected)

class TestSpellAPI(TransactionTestCase):

    def setUp(self):
        s1 = Spell.objects.create(
            id = 1,
            incantation = 'blah',
            alias = 'blah blah',
            effect = 'death',
            creator = 'me',
            notable_uses = 'Some',
            unforgivable = True,
            difficulty = 'Hard',
            kind = 'Transfiguration'
          )
        s2 = Spell.objects.create(
            id = 2,
            incantation = 'blah2',
            alias = 'blah blah',
            effect = 'death',
            creator = 'me',
            notable_uses = 'World cup',
            unforgivable = False,
            difficulty = 'Hard',
            kind = 'Transfiguration'
          )

    def testDetail(self):
        school = Spell.objects.get(pk=1)
        url = reverse('spell_api', kwargs={'id': 1})
        response = fetch_url(url)
        expected = { 
            'id': 1,
            'incantation': 'blah',
            'alias': 'blah blah',
            'effect': 'death',
            'creator': 'me',
            'notable_uses': 'Some',
            'unforgivable': True,
            'difficulty': 'Hard',
            'kind': 'Transfiguration',
            'creature': None
        } 
        self.assertEqual(response, expected)

    def testIndex(self):
        url = reverse('spells_api')
        response = fetch_url(url)
        expected = [{ 
            'id': 1,
            'incantation': 'blah',
            'alias': 'blah blah',
            'effect': 'death',
            'creator': 'me',
            'notable_uses': 'Some',
            'unforgivable': True,
            'difficulty': 'Hard',
            'kind': 'Transfiguration',
            'creature': None 
        }, {
            'id': 2,
            'incantation': 'blah2',
            'alias': 'blah blah',
            'effect': 'death',
            'creator': 'me',
            'notable_uses': 'World cup',
            'unforgivable': False,
            'difficulty': 'Hard',
            'kind': 'Transfiguration',
            'creature': None
          }]
        self.assertEqual(response, expected)

"""
  HAYSTACK SEARCH TESTS
"""

# Define a location for creating temporary search indexes of test fixture DB
TEST_INDEX = {
    'default': {
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_test_index'),
    },
}

def sqsToModelList(sqs):
    """
    Create a list of model instances from a list of haystack SearchResult 
    instances
    """
    return [sr.object for sr in sqs]

@override_settings(HAYSTACK_CONNECTIONS=TEST_INDEX)
class TestMultiAndSingleWordSearch(TestCase):

    # Snapshot of our real data
    fixtures = ['test_data.json']

    def setUp(self):
        super(TestMultiAndSingleWordSearch, self).setUp()
        haystack.connections.reload('default')
        call_command('rebuild_index', verbosity=0, interactive=False)

    def tearDown(self):
        call_command('clear_index', interactive=False, verbosity=0)

    def testSingleWord(self):
        # Single Word Search only generates OR results    
        or_sq = generateSearchQuery('felix', 'OR')
        or_sqs = SearchQuerySet().filter(or_sq)
        actual_results = sqsToModelList(or_sqs)

        expected_results = []
        expected_results += [Potion.objects.get(pk=3)]

        self.assertEqual(expected_results, actual_results)
    
    def testMultiWordOr(self):
        or_sq = generateSearchQuery('nearly headless', 'OR')
        or_sqs = SearchQuerySet().filter(or_sq)
        actual_results = sqsToModelList(or_sqs)

        expected_results = []
        expected_results += [Character.objects.get(pk=1)]
        expected_results += [Creature.objects.get(pk=1)]
        expected_results += [Story.objects.get(pk=3)]
        expected_results += [Spell.objects.get(pk=1)]
        expected_results += [Artifact.objects.get(pk=7)]
        expected_results += [Story.objects.get(pk=9)]
        
        self.assertEqual(len(or_sqs), len(expected_results))
        for expected_result in expected_results:
            self.assertTrue(expected_result in actual_results)

        # Nonsense word doesn't affect OR query
        or_sq_2 = generateSearchQuery('nearly headless junkyjunkword', 'OR')
        or_sqs_2 = SearchQuerySet().filter(or_sq_2)
        self.assertEqual(len(or_sqs_2), len(or_sqs))
        model_list = sqsToModelList(or_sqs_2)
        for v in or_sqs:
            self.assertTrue(v.object in model_list)

    def testMultiWordAnd(self):
        and_sq = generateSearchQuery('nearly headless', 'AND')
        and_sqs = SearchQuerySet().filter(and_sq)
        actual_results = sqsToModelList(and_sqs)

        expected_results = []
        expected_results += [Character.objects.get(pk=1)]
        expected_results += [Creature.objects.get(pk=1)]
        expected_results += [Story.objects.get(pk=3)]

        self.assertEqual(len(actual_results), 3)
        self.assertEqual(len(actual_results), len(expected_results))
        for expected_result in expected_results:
            self.assertTrue(expected_result in actual_results)

        # Nonsense word doesn't ruins AND search 
        and_sq_2 = generateSearchQuery('nearly headless junkyjunkword', 'AND')
        and_sqs_2 = SearchQuerySet().filter(and_sq_2)
        self.assertEqual(len(and_sqs_2), 0)

@override_settings(HAYSTACK_CONNECTIONS=TEST_INDEX)
class TestCharacterSearch(TestCase):

    # Snapshot of our real data
    fixtures = ['test_data.json']

    def setUp(self):
        super(TestCharacterSearch, self).setUp()
        haystack.connections.reload('default')
        call_command('rebuild_index', verbosity=0, interactive=False)

    def tearDown(self):
        call_command('clear_index', interactive=False, verbosity=0)

    def testNameSearchability(self):
        sq = generateSearchQuery('rowena', 'OR')
        sqs = SearchQuerySet().filter(sq)
        actual_results = sqsToModelList(sqs) 
        self.assertEqual(len(actual_results), 1)

        rowena = Character.objects.get(pk=49)
        self.assertEqual(rowena, actual_results[0])

    def testWandSearchability(self):
        sq = generateSearchQuery('15 inches elder wood with thestral hair', 'AND')
        sqs = SearchQuerySet().filter(sq)
        actual_results = sqsToModelList(sqs) 
        self.assertEqual(len(actual_results), 2)

        expected_results = []
        expected_results += [Character.objects.get(pk=6)]  # Dubledore
        expected_results += [Character.objects.get(pk=17)] # Grindlewald

        self.assertEqual(len(expected_results), len(actual_results))
        for expected_result in expected_results:
            self.assertTrue(expected_result in actual_results)

    def testQuotebySearchability(self):
        sq = generateSearchQuery('helena ravenclaw', 'AND')
        sqs = SearchQuerySet().filter(sq)
        actual_results = sqsToModelList(sqs) 
        self.assertEqual(len(actual_results), 2)

        # Helena Ravenclaw loved talking about ghosts
        expected_results = []
        expected_results += [Character.objects.get(pk=11)] # Bloody Baron
        expected_results += [Character.objects.get(pk=48)] # Grey Lady

        self.assertEqual(len(expected_results), len(actual_results))
        for expected_result in expected_results:
            self.assertTrue(expected_result in actual_results)

@override_settings(HAYSTACK_CONNECTIONS=TEST_INDEX)
class TestStorySearch(TestCase):

    # Snapshot of our real data
    fixtures = ['test_data.json']

    def setUp(self):
        super(TestStorySearch, self).setUp()
        haystack.connections.reload('default')
        call_command('rebuild_index', verbosity=0, interactive=False)

    def tearDown(self):
        call_command('clear_index', interactive=False, verbosity=0)

    def testNameSearchability(self):
        sq = generateSearchQuery('statute of international secrecy', 'AND')
        sqs = SearchQuerySet().filter(sq)
        actual_results = sqsToModelList(sqs) 

        statute = Story.objects.get(name='International Statute of Wizarding Secrecy')
        self.assertIn(statute, actual_results)

    def testDateSearchability(self):
        sq = generateSearchQuery('1692')
        sqs = SearchQuerySet().filter(sq)
        actual_results = sqsToModelList(sqs) 

        statute = Story.objects.get(name='International Statute of Wizarding Secrecy')
        self.assertIn(statute, actual_results)

    def testDescriptionSearchability(self):
        sq = generateSearchQuery('voldemort')
        sqs = SearchQuerySet().filter(sq)
        actual_results = sqsToModelList(sqs) 

        story1 = Story.objects.get(name='The Boy Who Lived')
        story2 = Story.objects.get(name='The Prophecy')

        self.assertIn(story1, actual_results)
        self.assertIn(story2, actual_results)