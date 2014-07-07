from django.test import TestCase
import library.models as lm

# Create your tests here.
class CreatureTest(TestCase):
    def test_create_creature(self):
        creature = lm.Creature()

        # set attributes
        creature.name = 'Goblin'
        creature.description = "Goblins are a highly intelligent race of small hominids with long fingers and feet that coexist with the wizard world.  Their diet consists of meat, roots and fungi. Goblins converse in a language known as Gobbledegook, and are adept metalsmiths notable for their silverwork; they even mint coins for wizarding currency. Due to their skills with money and finances, they control the wizarding economy to a large extent and run Gringotts Wizarding Bank.\n\nGoblins have their own type of magic and can do magic without a wand. They are represented by the Goblin Liaison Office of the Department for the Regulation and Control of Magical Creatures in the Ministry of Magic. Goblins are considered to be inferior by many wizards, who foolishly believe that the goblins are comfortable with that arrangement.  Goblins do not like Dolores Umbrige."
        creature.classification = 'Being'
        creature.rating = 3
        #TODO: test image

        creature.save()

        # Check that it works
        all_creatures = lm.Creature.objects.all()
        self.assertEquals(len(all_creatures), 1)
        only_creature = all_creatures[0]
        self.assertEquals(only_creature, creature) 

        # Check attributes
        self.assertEquals(only_creature.name, creature.name)
        self.assertEquals(only_creature.description, only_creature.description)
        self.assertEquals(only_creature.classification, creature.classification)
        self.assertEquals(only_creature.rating, creature.rating)

    def test_create_shop(self):
        shop = lm.Shop()
        shop.name = "Weasley's Wizard Wheezes"
        shop.description = "A practical magical joke shop run by the Weasley brothers. Well, one brother now..."
        shop.kind = 'shop'

        # Relationships
        location = lm.Location()
        location.name = 'Diagon Alley'
        location.save()
        shop.location = location
        shop.save()

        #character = lm.Character()
        #character.name = 'George Weasley'
        #character.shop = shop
        #character.save()

        first_shop = lm.Shop.objects.first()
        self.assertEquals(str(first_shop), shop.name)
        self.assertEquals(first_shop.name, shop.name)
        self.assertEquals(first_shop.description, shop.description)
        self.assertEquals(first_shop.kind, shop.kind)
        self.assertEquals(first_shop.location, location)
        #self.assertEquals(first_shop.owners.first, character)

    def test_create_location(self):
        location = lm.Location()
        location.name = 'Knockturn Alley'
        location.description = 'Only naughty wizards go here. Why are you here? You must be naughty.'
        location.kind = 'shopping district'
        location.save()

        first_location = lm.Location.objects.first()
        self.assertEquals(str(first_location), location.name)
        self.assertEquals(first_location.name, location.name)
        self.assertEquals(first_location.description, location.description)
        self.assertEquals(first_location.kind, location.kind)


