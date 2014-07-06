from django.db import models

# Create your models here.
class Character(models.Model):

class Spell(models.Model):

class Creature(models.Model):

class Potion(models.Model):

class Location(models.Model):

class School(Locations):

class Shop(Locations):

class Store(models.Model):

class Artifact(models.Model):
    name = models.CharField(max_field=100)
    description = models.TextField()
    kind = models.CharField(max_field=100)
    image = models.ImageField(upload_to="images/artifacts")
    owner = models.ForeignKey(Character)
    # Belongs to relationships get the foreign key

    def __str__(self):              
        return self.name

class Book(models.Model):
    name = models.CharField(max_field=100)
    description = models.TextField()
    author = models.ForeignKey(Character)

    def __str__(self):              
        return self.name

class AcademicStatus(models.Model):

class Relationship(models.Model):
