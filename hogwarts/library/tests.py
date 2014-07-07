from django.test import TestCase
import library.models as lm

# Create your tests here.
class CreatureTest(TestCase):
    def setUp(self):
        pass
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


    def test_string_creature(self):
        

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
    def test_create_potion(self):
        potion = Potion()
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
        potions = Potion.objects.all()
        self.assertEquals(len(potions), 1)
        potion_created = potions[0]
        self.assertEquals(potion, potion_created)
        
        
        self.assertEquals(name, potion.title)
        self.assertEquals(difficult, potion.difficulty)
        self.assertEquals(physical_description, potion.description)
        self.assertEquals(the_recipe, potion.recipe)
        self.assertEquals(effect, potion.effects)
        self.assertEquals(uses, potion.usages)
        self.assertEquals(more_information, potion.more_info)
