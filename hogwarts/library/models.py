from django.db import models

# Create your models here.
class Character(models.Model):

class Spell(models.Model):

class Creature(models.Model):

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

class School(Locations):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=20)
    description = models.TextField()
    

class House(models.Model):
    name = models.CharField(max_length=11)
    description = models.TextField()
    school = models.ForeignKey('School')

class Shop(Locations):

class Store(models.Model):

class Artifact(models.Model):

class Book(models.Model):

class AcademicStatus(models.Model):

class Relationship(models.Model):
