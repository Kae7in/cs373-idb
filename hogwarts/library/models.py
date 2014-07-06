from django.db import models

# Create your models here.
class Characters(models.Model):
    pass

class Spells(models.Model):
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

class Story(models.Model):
    pass

class Artifacts(models.Model):
    pass

class Books(models.Model):
    pass

class AcademicStatuses(models.Model):
    pass

class Relationships(models.Model):
    pass
