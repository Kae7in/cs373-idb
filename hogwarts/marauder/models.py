from django.db import models
# Create your models here.
class Character(models.Model):
    #descriptors
    character_id = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    birthday = models.CharField(max_length = 100)
    description = models.TextField()
    magical = models.BooleanField(default=True)
    quotes = models.TextField()
    images = models.ImageField(upload_to = 'images/characters', default = 'images/empty.jpg')

    #relationships
    creature = models.ForeignKey('Creature', related_name="characters", blank=True, null=True)
    shop = models.ForeignKey('Shop', related_name="owners", blank=True, null=True)

    def is_squib(self):
        for relation in self.relationships.all():
            if(relation.character1 == self):
                other_id = relation.character2
                other_desc = relation.descriptor2
            else:
                other_id = relation.character1.id
                other_desc = relation.descriptor1
            if(other_desc == 'mother' or other_desc == 'father'):
                parent = Character.objects.get(pk=other_id)
                if(parent.magical):
                    return True
        return False

class Creature(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    CLASS_CHOICES = (('Beast', 'Beast'),
                     ('Being', 'Being'),
                     ('NB', 'Non-being'),
                     ('Spirit', 'Spirit'))
    classification = models.CharField(max_length=6, choices=CLASS_CHOICES)
    RATING_CHOICES = ((0, 'Unknown'), (1,'X'),(2,'XX'),(3,'XXX'),(4,'XXXX'),(5,'XXXXX'))
    rating = models.IntegerField(choices=RATING_CHOICES)
    image = models.ImageField(upload_to='images/creatures')

    def __str__(self):
        return self.name

    def potions(self):
        return creature.ingredients.first().potions.all()

    def neutralize(self, incantation):
        return self.spells.first().incantation == incantation

class Spell(models.Model):
    incantation = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    effect = models.TextField()
    creator = models.CharField(max_length=50)
    notable_uses = models.TextField()
    unforgivable = models.BooleanField(default=False)
    KIND_CHOICES = (('Transfiguration', 'Transfiguration'),
                    ('Charm', 'Charm'),
                    ('Jinx', 'Jinx'),
                    ('Hex', 'Hex'),
                    ('Curse', 'Curse'),
                    ('Defensive', 'Defensive'),
                    ('Healing', 'Healing'))
    kind = models.CharField(max_length=20, choices=KIND_CHOICES)
    image = models.ImageField(upload_to='images/spells')

    # affects certain creatures
    creature = models.ForeignKey('Creature', blank=True, null=True, related_name='spells')

    def __str__(self):
        return self.incantation

class Ingredient(models.Model):
    name = models.CharField(max_length = 100)
    creature = models.ForeignKey('Creature', null=True, blank=True, related_name = 'ingredients')

class Potion(models.Model):

    DIFFICULTIES = (
        ('E', 'Easy'),
        ('M', 'Moderate'),
        ('A', 'Advanced'),
    )
    title = models.CharField(max_length = 100)
    difficulty = models.CharField(max_length = 1, choices = DIFFICULTIES)
    description = models.TextField()
    effects = models.TextField()
    recipe = models.TextField()
    usages = models.TextField()
    more_info = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, related_name = 'potions', null=True, blank=True)
    image = models.ImageField(upload_to = 'images/potions', default = 'images/empty.jpg')
    characters = models.ManyToManyField(Character, related_name = 'potions', blank=True, null=True)
    other_potions = models.ManyToManyField('Potion', related_name = 'potions', blank=True, null=True)

    def __str__(self):
        return self.title

    def brew(self, available_ingredients):
        for required in self.ingredients.all():
            if(not required.name in available_ingredients):
                return 'Failure'
        if(self.ingredients.all().count() == len(available_ingredients)):
            return 'Success'
        return 'Explosion!'

class Location(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    kind = models.CharField(max_length=20)
    image = models.ImageField(upload_to = 'images/locations', default = 'images/empty.jpg')

    def __str__(self):
        return self.name

class School(Location):
    country = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class House(School):
    school = models.ForeignKey(School, related_name = 'child_houses')
    
    def __str__(self):
        return self.name

class Shop(Location):
    location = models.ForeignKey(Location, related_name = 'child_shops', blank=True, null=True)

class Artifact(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    kind = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='images/artifacts', default='images/empty.jpg')
    owner = models.ForeignKey(Character, related_name = 'artifacts', blank=True, null=True)
    shop  = models.ForeignKey(Shop, related_name='artifacts', blank=True, null=True)

    def __str__(self):              
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(Character, related_name = 'books', blank=True, null=True)

    def __str__(self):              
        return self.name

class Story(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    book = models.ForeignKey(Book, related_name = 'story', null=True, blank=True)
    kind = models.CharField(max_length=20)
    characters = models.ManyToManyField('Character', related_name = 'stories')
    artifacts = models.ManyToManyField('Artifact', related_name = 'stories')
    locations = models.ManyToManyField('Location', related_name = 'stories')

    def century(self):
        return self.date.year // 100 + 1

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'stories'

class Academic(models.Model):
    DESCRIPTORS = (
        ('founder', 'founder'),
        ('student', 'student'),
        ('professor', 'professor'),
        ('headmaster', 'headmaster'),
        ('staff', 'staff')
    )
    character = models.ForeignKey(Character, related_name = 'academic_statuses', blank=True, null=True)
    school = models.ForeignKey(School, related_name = 'academic_statuses', blank=True, null=True)
    descriptor = models.CharField(max_length=10, choices=DESCRIPTORS)

class Relationship(models.Model):
    #descriptors
    relation_id = models.CharField(max_length = 100)

    #relationships
    character1 = models.ForeignKey(Character, related_name = "relationship1", blank=True, null=True)
    character2 = models.ForeignKey(Character, related_name = "relationship2", blank=True, null=True)
    descriptor1 = models.TextField()
