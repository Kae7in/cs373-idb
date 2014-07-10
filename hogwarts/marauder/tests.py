from django.test import TestCase
import marauder.models as lm
from datetime import date

# Create your tests here.
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
        r1.descriptor1 = 'son'
        r1.character2 = dad
        r1.descriptor2 = 'father'
        r1.save()

        r2 = lm.Relationship()
        r2.character1 = mom
        r2.descriptor1 = 'mother'
        r2.character2 = argus
        r2.descriptor2 = 'son'
        r2.save()

        self.assertTrue(argus.is_squib)

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

        self.assertFalse(harry.is_squib)
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

        self.assertFalse(malfoy.is_squib)
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
        shop.location = location
        shop.save()

        first_shop = lm.Shop.objects.first()
        self.assertEqual(first_shop.location, location)

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
        artifact.owner = wizzy
        artifact.shop = shop
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

    def test_artifact_owner(self):
        a = lm.Artifact.objects.first()
        w = lm.Character.objects.first()
        self.assertEqual(a.owner, w)
        # self.assertIs(a.owner, w) # TODO: Why are they different instances?

        # Reverse lookup. 
        artifact = w.artifacts.first()
        self.assertEqual(artifact, a)

    def test_artifact_shop(self):
        a = lm.Artifact.objects.first()
        s = lm.Shop.objects.first()
        self.assertEqual(a.shop, s)
        self.assertEqual(a.shop.name, "Weasleys' Wizard Wheezes")
        # self.assertIs(a.owner, w) # TODO: Why are they different instances?

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

    def test_book_author(self):
        book   = lm.Book.objects.first()
        author = lm.Character.objects.first()
        self.assertEqual(book.author, author)
        self.assertEqual(author.books.first(), book)

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
        char2.name = "Ron Weasley" 
        char2.save()
        rel = lm.Relationship()
        rel.character1 = char1
        rel.character2 = char2
        rel.descriptor1 = "BEST FRIENDS FOREVER! <3"
        rel.save()
        

    def test_create_relationship(self):
        rel = lm.Relationship.objects.first()
        self.assertEqual(rel.character1, lm.Character.objects.first())
        self.assertEqual(rel.character2, lm.Character.objects.all()[1])
        self.assertEqual(rel.descriptor1, "BEST FRIENDS FOREVER! <3")
        
    def test_create_relationship2(self):
        rel = lm.Relationship.objects.first()
        self.assertEqual(rel.character1.name, lm.Character.objects.first().name)
        self.assertEqual(rel.character2.name, lm.Character.objects.all()[1].name)

class AcademicTest(TestCase):
    def setUp(self):
        snape = lm.Character()
        snape.name = "Severus Snape"
        snape.save()
        hogwarts = lm.School()
        hogwarts.name = "Hogwarts School of Witchcraft and Wizardry"
        hogwarts.save()
        
        academic = lm.Academic()
        academic.school = hogwarts
        academic.character = snape
        academic.descriptor = "professor"
        academic.save()

    def test_create_academic(self):
        academic = lm.Academic.objects.first()
        self.assertEqual(academic.character.name, "Severus Snape")
        self.assertEqual(academic.descriptor, "professor")
        self.assertEqual(academic.school.name, "Hogwarts School of Witchcraft and Wizardry")

    def test_create_academic2(self):
        academic = lm.Academic.objects.first()
        self.assertEqual(academic.character, lm.Character.objects.first())
        self.assertEqual(academic.school, lm.School.objects.first())  
