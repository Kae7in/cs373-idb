from django.db import models

# Create your models here.
class Characters(models.Model):
    pass
class Spell(models.Model):
    incantation = models.CharField(max_length=50)
    aliases = models.CharField(max_length=50)
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

class Creature(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    CLASS_CHOICES = (('Beast', 'Beast'),
                     ('Being', 'Being'),
                     ('Spirit', 'Spirit'))
    classification = models.CharField(max_length=6, choices=CLASS_CHOICES)
    RATING_CHOICES = ((x,x) for x in range(1,6))
    rating = models.IntegerField(choices=RATING_CHOICES)
    image = models.ImageField(upload_to='images/creatures')

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
class Artifacts(models.Model):
    pass
class Books(models.Model):
    pass
class AcademicStatuses(models.Model):
    pass
class Relationships(models.Model):
    pass
