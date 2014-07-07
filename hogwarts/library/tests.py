from django.test import TestCase
from library.models import Creature
from library.models import Potion
from library.models import School
from library.models import House

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
