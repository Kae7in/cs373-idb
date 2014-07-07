from django.test import TestCase
import library.models as lm
from datetime import date

# Create your tests here.
class CreatureTest(TestCase):
    def test_create_creature(self):
        creature = lm.Creature()

        # set attributes
        creature.name = 'Goblin'
        creature.description = "Goblins are a highly intelligent race of small hominids with long fingers and feet that coexist with the wizard world.\n"
        creature.classification = 'Being'
        creature.rating = 3
        #TODO: test image

        creature.save()

        # Check that it works
        all_creatures = lm.Creature.objects.all()
        self.assertEqual(len(all_creatures), 1)
        only_creature = all_creatures[0]
        self.assertEqual(only_creature, creature) 

        # Check attributes
        self.assertEqual(only_creature.name, creature.name)
        self.assertEqual(only_creature.description, only_creature.description)
        self.assertEqual(only_creature.classification, creature.classification)
        self.assertEqual(only_creature.rating, creature.rating)

class ShopTest(TestCase):
    def setUp(self):
        shop = lm.Shop()
        shop.name = "Weasley's Wizard Wheezes"
        shop.description = "A practical magical joke shop run by the Weasley brothers. Well, one brother now..."
        shop.kind = 'shop'
        shop.save()

    def test_create_shop(self):
        shop = lm.Shop.objects.first()
        self.assertEquals(shop.name, "Weasley's Wizard Wheezes")
        self.assertEquals(shop.description, "A practical magical joke shop run by the Weasley brothers. Well, one brother now...")
        self.assertEquals(shop.kind, 'shop')

    def test_relationships_shop(self):
        shop = lm.Shop.objects.first()
        location = lm.Location()
        location.name = 'Diagon Alley'
        location.save()
        shop.location = location
        shop.save()

        character = lm.Character()
        character.name = 'George Weasley'
        character.shop = shop
        character.save()

        first_shop = lm.Shop.objects.first()
        self.assertEquals(first_shop.location, location)
        self.assertEquals(first_shop.owners.first, character)

    def test_string_shop(self):
        shop = lm.Shop.objects.first()
        self.assertEquals(str(shop), shop.name)

class LocationTest(TestCase):
    def setUp(self):
        location = lm.Location()
        location.name = 'Knockturn Alley'
        location.description = 'Only naughty wizards go here. Why are you here? You must be naughty.'
        location.kind = 'shopping district'
        location.save() 

    def test_create_location(self):
        location = lm.Location.objects.first()
        self.assertEquals(location.name, 'Knockturn Alley')
        self.assertEquals(location.description, 'Only naughty wizards go here. Why are you here? You must be naughty.')
        self.assertEquals(location.kind, 'shopping district')

    def test_string_location(self):
        location = lm.Location.objects.first()
        self.assertEquals(str(location), location.name)

class StoryTest(TestCase):
    def test_create_story(self):
        story = lm.Story()
        story.name = 'Deathly Hallows'
        story.description = 'There were three brothers and they all died.'
        story.kind = 'legend'
        story.date = date(1200, 1, 1)

        book = lm.Book()
        book.name = 'The Tales of Beedle the Bard'
        book.save()
        story.book = book

        elder_wand = lm.Artifact()
        elder_wand.save()
        book.artifacts.add(elder_wand)

        ignotus = lm.Character()
        ignotus.name = 'Ignotus Peverell'
        ignotus.save()
        book.characters.add(ignotus)

class SpellTest(TestCase):
    def test_create_spell(self):
        spell = lm.Spell()

        # set attributes
        spell.incantation = 'Expecto Patronum'
        spell.alias = 'Patronus Charm'
        spell.effect = 'evokes a partially-tangible positive energy force known as a Patronus (pl. Patronuses) or spirit guardian'
        spell.notable_uses = 'Yes. Harry used it for dementors.'
        spell.unforgivable = False 
        spell.kind = 'Charm'
        #TODO: test image

        spell.save()

        # Check that it works
        all_spells = lm.Spell.objects.all()
        self.assertEqual(len(all_spells), 1)
        only_spell = all_spells[0]
        self.assertEqual(only_spell, spell) 

        # Check attributes
        self.assertEqual(only_spell.incantation, spell.incantation)
        self.assertEqual(only_spell.alias, only_spell.alias)
        self.assertEqual(only_spell.effect, spell.effect)
        self.assertEqual(only_spell.notable_uses, spell.notable_uses)
        self.assertEqual(only_spell.unforgivable, spell.unforgivable)
        self.assertEqual(only_spell.kind, spell.kind)

class PotionTest(TestCase):

    def setUp(self):
        
        potion = lm.Potion()
        potion.title = "Felix Felices"
        potion.difficulty = 'A'
        potion.description = "Its color is molten gold..."
        potion.recipe = 'Add to the cauldron an Ashwinder egg and horseradish before heating...'
        potion.effects = "Increases the drinker's luck. Overdose can..."
        potion.usages = "Hermoine, Ginny and Ron used Felix Felices to evade the curses of Death Eaters..."
        potion.more_info = "Also called \"Liquid Luck\", Felix Felices was invented..."
        potion.save()
    
    def test_create_potion(self):
        potions = lm.Potion.objects.all()
        self.assertEquals(len(potions), 1)
        potion_created = potions.first()
        
        
        self.assertEquals("Felix Felices", potion_created.title)
        self.assertEquals("A", potion_created.difficulty)
        self.assertEquals("Its color is molten gold...", potion_created.description)
        self.assertEquals("Add to the cauldron an Ashwinder egg and horseradish before heating...", potion_created.recipe)
        self.assertEquals("Increases the drinker's luck. Overdose can...", potion_created.effects)
        self.assertEquals("Hermoine, Ginny and Ron used Felix Felices to evade the curses of Death Eaters...", potion_created.usages)
        self.assertEquals("Also called \"Liquid Luck\", Felix Felices was invented...", potion_created.more_info)
        self.assertEquals("images/empty.jpg", potion_created.image)
        all_creatures = potion_created.creatures.all()
        self.assertEquals(len(all_creatures), 0)

    def test_string_potion(self):
        potion = lm.Potion.objects.all().first()
        self.assertEquals(str(potion), "Felix Felices")

    def test_potion_image(self):
        potion = lm.Potion.objects.all().first()
        potion.image = "images/non_empty.jpg"
        potion.save()

    def test_potion_creatures(self):
        potion = lm.Potion.objects.first()
        creature1 = lm.Creature()
        creature1.name = "Hippogriff"
        creature1.description = "uh"
        creature1.classification = "Beast"
        creature1.rating = 1
        creature1.image = "images/non_empty.jpg"
        creature1.save()
        creature2 = lm.Creature()
        creature2.name = "Hippogriff"
        creature2.description = "uh"
        creature2.classification = "Beast"
        creature2.rating = 1
        creature2.image = "images/non_empty.jpg"
        creature2.save()
        potion.creatures = [creature1, creature2]
        potion.save()
        self.assertEquals(potion.creatures.all()[0], creature1)
        self.assertEquals(potion.creatures.all()[1], creature2)

class SchoolTest(TestCase):

    def setUp(self):
      
        school = lm.School()
        name = "Durmstrang Institute"
        school.name = name
        description = "These guys don't really like muggle-borns very much. Except Krum I guess."
        school.description = description
 
        school.save()

    def test_create_school(self):
        
        schools = lm.School.objects.all()
        self.assertEquals(len(schools), 1)
        school_created = schools.first()
        self.assertEquals(school_created, school_created)
        self.assertEquals("Durmstrang Institute", school_created.name)
        self.assertEquals("These guys don't really like muggle-borns very much. Except Krum I guess.", school_created.description)
        self.assertEquals("images/empty.jpg", school_created.image)

    def test_school_string(self):
        school = lm.School.objects.first()
        self.assertEqual(str(school), "Durmstrang Institute")	
	
    def test_school_image(self):	
        school = lm.School.objects.first()
        school.image = "images/non_empty.jpg"
        school.save()
        self.assertEqual(school.image, "images/non_empty.jpg")	 

class HouseTest(TestCase):

    def setUp(self):
    
        house = lm.House()
        house.name = "Hufflepuff"
        house.description = "Nobody wants to be a Hufflepuff."

        school2 = lm.School()
        school2.name = "Hogwarts"
        school2.description = "The best school ever"
        school2.save()
        house.school = school2
        house.save()
    
    def test_create_house(self):
        houses = lm.House.objects.all()
        self.assertEquals(len(houses), 1)
        house_created = houses.first()
        self.assertEquals(house_created, house_created)
        
        
        self.assertEquals("Hufflepuff", house_created.name)
        self.assertEquals("Nobody wants to be a Hufflepuff.", house_created.description)
        self.assertEquals("images/empty.jpg", house_created.image)

    def test_house_string(self):
        house = lm.House.objects.first()
        self.assertEquals(str(house), "Hufflepuff")

    def test_house_image(self):
        house = lm.House.objects.first()
        house.image = "images/non_empty.jpg"
        house.save()
        self.assertEqual(house.image, "images/non_empty.jpg")	

class ArtifactTest(TestCase):
    def setUp(self):
        self.artifact  = lm.Artifact()
        self.wizzy = lm.Character()

        self.wizzy.name = "Some Wizard"
        self.wizzy.save()

        self.artifact.name = "Pensieve"
        self.artifact.description = "The Pensieve is an object used to review memories. It has the appearance of a shallow stone basin, into which are carved runes and strange symbols. It is filled with a silvery substance that appears to be a cloud-like liquid/gas; the collected memories of people who have siphoned their recollections into it. Memories can then be viewed from a non-participant, third-person point of view."
        # TODO: Test kind
        # TODO: Test image
        self.artifact.owner = wizzy
        self.artifact.save()

    def test_create_artifact(self):
        artifacts = self.artifacts.objects.all()
        self.assertEquals(len(artifacts), 1)
        a = artifacts[0]
        self.assertEquals(len(artifacts[0]), 1)
        self.assertEquals(a.name, "Pensieve")
        self.assertEquals(a.description, "The Pensieve is an object used to review memories. It has the appearance of a shallow stone basin, into which are carved runes and strange symbols. It is filled with a silvery substance that appears to be a cloud-like liquid/gas; the collected memories of people who have siphoned their recollections into it. Memories can then be viewed from a non-participant, third-person point of view.")
        self.assertEquals(a.image, "images/empty.jpg")
