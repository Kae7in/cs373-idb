from django.db import models

# Create your models here.
class Character(models.Model):
    pass

class Spell(models.Model):
    pass

class Creature(models.Model):
    pass
 
class Potion(models.Model):
    pass

class Location(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    kind = models.CharField(max_length=20)
    image = models.ImageField(upload_to = 'images/locations', default = 'images/empty.jpg')


class School(Location):
    pass

class Shop(Location):
    location = models.ForeignKey(Location, related_name = 'child_shops')

class Artifact(models.Model):
    pass

class Book(models.Model):
    pass

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