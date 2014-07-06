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
    name = models.CharField(max_length=40)
    description = models.TextField()
    kind = models.CharField(max_length=20)
    image = models.ImageField(upload_to = 'images/locations', default = 'images/empty.jpg')

class Schools(Locations):
    pass

class Shops(Locations):
    location = models.ForeignKey('Locations', related_name = 'child_shops')

class Stores(models.Model):
    pass

class Artifacts(models.Model):
    pass

class Books(models.Model):
    pass

class AcademicStatuses(models.Model):
    pass

class Relationships(models.Model):
    pass