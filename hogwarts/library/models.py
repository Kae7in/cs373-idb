from django.db import models

# Create your models here.
class Character(models.Model):
    pass

class Spell(models.Model):
    incantation = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)
    effect = models.TextField()
    notable_uses = models.TextField()
    unforgivable = models.BooleanField()
    KIND_CHOICES = (('Transfiguration', 'Transfiguration'),
                    ('Charm', 'Charm'),
                    ('Jinx', 'Jinx'),
                    ('Hex', 'Hex'),
                    ('Curse', 'Curse'),
                    ('Defensive', 'Defensive'),
                    ('Healing', 'Healing'))
    kind = models.CharField(max_length=20, choices=KIND_CHOICES)
    image = models.ImageField(upload_to='images/spells')

    def __str__(self):
        return self.incantation

class Creature(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    CLASS_CHOICES = (('Beast', 'Beast'),
                     ('Being', 'Being'),
                     ('Spirit', 'Spirit'))
    classification = models.CharField(max_length=6, choices=CLASS_CHOICES)
    RATING_CHOICES = ((1,'X'),(2,'XX'),(3,'XXX'),(4,'XXXX'),(5,'XXXXX'))
    rating = models.IntegerField(choices=RATING_CHOICES)
    image = models.ImageField(upload_to='images/creatures')

    def __str__(self):
        return self.name

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
    creatures = models.ManyToManyField(Creature)
    image = models.ImageField(upload_to = 'images/potions', default = 'images/empty.jpg')

class Location(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    kind = models.CharField(max_length=20)
    image = models.ImageField(upload_to = 'images/locations', default = 'images/empty.jpg')

class School(Location):
    country = models.CharField(max_length=20)
    
class House(School):
    school = models.ForeignKey('School', related_name = 'child_houses')

class Shop(Location):
    location = models.ForeignKey(Location, related_name = 'child_shops')

class Artifact(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    kind = models.CharField(max_length=100)
    image = models.ImageField(upload_to="images/artifacts")
    owner = models.ForeignKey(Character)

    def __str__(self):              
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(Character)

    def __str__(self):              
        return self.name

class Story(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    book = models.ForeignKey(Book)
    characters = models.ManyToManyField(Character)
    artifacts = models.ManyToManyField(Artifact)
    locations = models.ManyToManyField(Location)

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
    character = models.ForeignKey(Character)
    school = models.ForeignKey(School)
    descriptor = models.CharField(max_length=10, choices=DESCRIPTORS)

class Relationship(models.Model):
    pass
