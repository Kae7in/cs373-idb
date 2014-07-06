from django.db import models

# Create your models here.
class Character(models.Model):
    pass

class Spell(models.Model):
    pass

class Creature(models.Model):
    pass
 
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
    name = models.CharField(max_field=100)
    description = models.TextField()
    kind = models.CharField(max_field=100)
    image = models.ImageField(upload_to="images/artifacts")
    owner = models.ForeignKey(Character)

    def __str__(self):              
        return self.name

class Book(models.Model):
    name = models.CharField(max_field=100)
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

class AcademicStatus(models.Model):
    pass

class Relationship(models.Model):
    pass