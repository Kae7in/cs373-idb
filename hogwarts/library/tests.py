from django.test import TestCase
import library.models as lm
from datetime import date

# Create your tests here.
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

    def test_string_creature(self):
        creature = lm.Creature.objects.first()
        self.assertEqual(str(creature), creature.name)    

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

    def test_relationships_shop(self):
        shop = lm.Shop.objects.first()
        location = lm.Location()
        location.name = 'Diagon Alley'
        location.save()
        shop.location = location
        shop.save()

        character = lm.Character()
        character.name = 'George Weasley'
        character.magical = True
        character.shop = shop
        character.save()

        first_shop = lm.Shop.objects.first()
        self.assertEqual(first_shop.location, location)
        self.assertEqual(first_shop.owners.first, character)

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
    def setUp(self):
        spell = lm.Spell()
        spell.incantation = 'Expecto Patronum'
        spell.alias = 'Patronus Charm'
        spell.effect = "evokes a positive energy force"
        spell.notable_uses = "Harry used it for dementors."
        spell.unforgivable = False 
        spell.kind = 'Charm'
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
        potion.description = "Its color is molten gold..."
        potion.recipe = 'Add to the cauldron an Ashwinder egg and horseradish before heating...'
        potion.effects = "Increases the drinker's luck. Overdose can..."
        potion.usages = "Hermoine, Ginny and Ron used Felix Felices to evade the curses of Death Eaters..."
        potion.more_info = "Also called \"Liquid Luck\", Felix Felices was invented..."
        potion.save()
    
    def test_create_potion(self):
        potions = lm.Potion.objects.all()
        self.assertEqual(len(potions), 1)
        potion_created = potions.first()
        
        
        self.assertEqual("Felix Felices", potion_created.title)
        self.assertEqual("A", potion_created.difficulty)
        self.assertEqual("Its color is molten gold...", potion_created.description)
        self.assertEqual("Add to the cauldron an Ashwinder egg and horseradish before heating...", potion_created.recipe)
        self.assertEqual("Increases the drinker's luck. Overdose can...", potion_created.effects)
        self.assertEqual("Hermoine, Ginny and Ron used Felix Felices to evade the curses of Death Eaters...", potion_created.usages)
        self.assertEqual("Also called \"Liquid Luck\", Felix Felices was invented...", potion_created.more_info)
        self.assertEqual("images/empty.jpg", potion_created.image)
        all_creatures = potion_created.creatures.all()
        self.assertEqual(len(all_creatures), 0)

    def test_string_potion(self):
        potion = lm.Potion.objects.all().first()
        self.assertEqual(str(potion), "Felix Felices")

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
        self.assertEqual(potion.creatures.all()[0], creature1)
        self.assertEqual(potion.creatures.all()[1], creature2)

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
        self.assertEqual(len(schools), 1)
        school_created = schools.first()
        self.assertEqual(school_created, school_created)
        self.assertEqual("Durmstrang Institute", school_created.name)
        self.assertEqual("These guys don't really like muggle-borns very much. Except Krum I guess.", school_created.description)
        self.assertEqual("images/empty.jpg", school_created.image)

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
        self.assertEqual(len(houses), 1)
        house_created = houses.first()
        self.assertEqual(house_created, house_created)
        
        
        self.assertEqual("Hufflepuff", house_created.name)
        self.assertEqual("Nobody wants to be a Hufflepuff.", house_created.description)
        self.assertEqual("images/empty.jpg", house_created.image)

    def test_house_string(self):
        house = lm.House.objects.first()
        self.assertEqual(str(house), "Hufflepuff")

    def test_house_image(self):
        house = lm.House.objects.first()
        house.image = "images/non_empty.jpg"
        house.save()
        self.assertEqual(house.image, "images/non_empty.jpg")	
