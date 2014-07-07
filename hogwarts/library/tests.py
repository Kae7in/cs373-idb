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
    def test_create_potion(self):
        potion = lm.Potion()
        name = "Amortentia"
        potion.title = name
        difficult = 'A'
        potion.difficulty = difficult
        physical_description = 'Its color is molten gold. When inside a cauldron, drops of the liquid will leap above the surface.'
        potion.description = physical_description
        the_recipe = 'Add to the cauldron an Ashwinder egg and horseradish before heating. Then add a juiced squill bulb and stir. Add chopped Murtlap tentacle to mixture and heat again. Then add a dash of tincture of thyme before stirring slowly. Add ground Occamy eggshell. Stir slowly and heat again. Sprinkle powdered common rue over the  mixture before stirring and heating again. Then make a figure-eight motion over the cauldron with the wand and say the incantation, "Felixempra!". Needs to be brewed for six months.'
        potion.recipe = the_recipe
        effect = "Increases the drinker's luck. Overdose can induce giddiness and recklessness. Large quantities can be toxic."
        potion.effects = effect
        uses = "Hermoine, Ginny and Ron used Felix Felices to evade the curses of Death Eaters.  Horace Slughorn used this potion at 24and 57 years old. It gave him one perfect day each time. Professor Slughorn awarded Harry enough potion for 12 hours' worth of luck for producing the most effective Draught of Living Death potion of anyone in his class."
        potion.usages = uses
        more_information = "Also called \"Liquid Luck\", Felix Felices was invented by Zygmunt Budge in the 16th century. The drinker of the potion is given the best scenario possible in their situation, which manifests in an urge or a voice telling them which action to take to ensure the outcome."
         
        potion.more_info = more_information
        potion.save()
        potions = lm.Potion.objects.all()
        self.assertEquals(len(potions), 1)
        potion_created = potions[0]
        self.assertEquals(potion, potion_created)
        
        
        self.assertEquals(name, potion_created.title)
        self.assertEquals(difficult, potion_created.difficulty)
        self.assertEquals(physical_description, potion_created.description)
        self.assertEquals(the_recipe, potion_created.recipe)
        self.assertEquals(effect, potion_created.effects)
        self.assertEquals(uses, potion_created.usages)
        self.assertEquals(more_information, potion_created.more_info)
        self.assertEquals("images/empty.jpg", potion_created.image)
        all_creatures = potion_created.creatures.all()
        self.assertEquals(len(all_creatures), 0)

class SchoolTest(TestCase):
    def test_create_school(self):
        school = School()
        name = "Durmstrang Institute"
        school.name = name
        description = "These guys don't really like muggle-borns very much. Except Krum I guess."
        school.description = description
 
        school.save()
        
        schools = School.objects.all()
        self.assertEquals(len(schools), 1)
        school_created = schools[0]
        self.assertEquals(school, school_created)
        
        
        self.assertEquals(name, school_created.name)
        self.assertEquals(description, school_created.description)
        self.assertEquals("images/empty.jpg", school_created.image)

class HouseTest(TestCase):
    def test_create_house(self):
        house = House()
        name = "Hufflepuff"
        description = "Nobody wants to be a Hufflepuff."

        house.name = name
        house.description = description
        school2 = School()
        school2.name = "Hogwarts"
        school2.description = "The best school ever"
        school2.save()
        house.school = school2
        house.save()
        houses = House.objects.all()
        self.assertEquals(len(houses), 1)
        house_created = houses[0]
        self.assertEquals(house, house_created)
        
        
        self.assertEquals(name, house_created.name)
        self.assertEquals(description, house_created.description)
        self.assertEquals("images/empty.jpg", house_created.image)
