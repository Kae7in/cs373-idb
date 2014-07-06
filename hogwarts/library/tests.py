from django.test import TestCase
from library.models import Creature

# Create your tests here.
class CreatureTest(TestCase):
    def test_create_creature(self):
        creature = Creature()

        # set attributes
        creature.name = 'Goblin'
        creature.description = "Goblins are a highly intelligent race of small hominids with long fingers and feet that coexist with the wizard world.  Their diet consists of meat, roots and fungi. Goblins converse in a language known as Gobbledegook, and are adept metalsmiths notable for their silverwork; they even mint coins for wizarding currency. Due to their skills with money and finances, they control the wizarding economy to a large extent and run Gringotts Wizarding Bank.\n\nGoblins have their own type of magic and can do magic without a wand. They are represented by the Goblin Liaison Office of the Department for the Regulation and Control of Magical Creatures in the Ministry of Magic. Goblins are considered to be inferior by many wizards, who foolishly believe that the goblins are comfortable with that arrangement.  Goblins do not like Dolores Umbrige."
        creature.classification = 'Being'
        creature.rating = 3
        #TODO: test image

        creature.save()

        # Check that it works
        all_creatures = Creature.objects.all()
        self.assertEquals(len(all_creatures), 1)
        only_creature = all_creatures[0]
        self.assertEquals(only_creature, creature) 

        # Check attributes
        self.assertEquals(only_creature.name, creature.name)
        self.assertEquals(only_creature.description, only_creature.description)
        self.assertEquals(only_creature.classification, creature.classification)
        self.assertEquals(only_creature.rating, creature.rating)
