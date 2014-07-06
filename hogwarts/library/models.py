from django.db import models

# Create your models here.
class Characters(models.Model):
    pass

class Spells(models.Model):
    pass

class Creatures(models.Model):
    pass

class Potions(models.Model):
    pass

class Locations(models.Model):
    pass

class Schools(Locations):
    pass

class Shops(Locations):
    pass

class Stores(models.Model):
    pass

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

class AcademicStatuses(models.Model):
    pass

class Relationships(models.Model):
    pass
