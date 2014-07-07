from django.test import TestCase
import library.models as lm

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

