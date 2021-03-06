from django.db import models
from django.core.urlresolvers import reverse
import inflect
# Create your models here.
class Character(models.Model):
    #descriptors
    name = models.CharField(max_length = 100)
    wand = models.CharField(max_length = 150, null=True, blank=True)
    description = models.TextField()
    magical = models.BooleanField(default=True)
    SEX_CHOICES = (('F', 'Female'),
                     ('M', 'Male'),
                     ('NB', 'Non-binary'))
    sex = models.CharField(max_length=2, choices=SEX_CHOICES)
    quote = models.TextField()
    quote_by = models.CharField(max_length = 200)
    image = models.ImageField(upload_to = 'images/', default = 'images/empty.jpg')

    #relationships
    creature = models.ForeignKey('Creature', blank=True, null=True, related_name = 'characters')
    house = models.ForeignKey('House', blank=True, null=True, related_name = 'members')
    school_attended = models.ForeignKey('School', blank=True, null=True, related_name = 'students')
    school_taught = models.ForeignKey('School', blank=True, null=True, related_name = 'professors')
    school_headmastered = models.ForeignKey('School', blank=True, null=True, related_name = 'headmasters')
    school_founded = models.ForeignKey('School', blank=True, null=True, related_name = 'founders')
    school_staffed = models.ForeignKey('School', blank=True, null=True, related_name = 'staff')
    shop = models.ForeignKey('Shop', blank=True, null=True, related_name='owners')

    hidden = models.BooleanField(default=False)

    def relationships(self):
        relationships = []
        for relation in self.relationships1.all():
            relationships.append(relation)
        for relation in self.relationships2.all():
            relationships.append(relation)
        return relationships

    def is_squib(self):
        if(self.magical == True):
            return False
        magic_parents = 0
        for relation in self.relationships():
            if(relation.character1 == self):
                other_id = relation.character2.id
                other_desc = relation.descriptor2
            else:
                other_id = relation.character1.id
                other_desc = relation.descriptor1
            if(other_desc.lower() == 'mother' or other_desc.lower() == 'father'):
                parent = Character.objects.get(pk=other_id)
                if(parent.magical):
                    magic_parents += 1
        return magic_parents == 2

    def get_absolute_url(self):
        return reverse('character', args=[self.id]) 

    def __str__(self):
        return self.name

class Creature(models.Model):
    name = models.CharField(max_length=50)
    plural = models.CharField(max_length=50)
    description = models.TextField()
    CLASS_CHOICES = (('Beast', 'Beast'),
                     ('Being', 'Being'),
                     ('NB', 'Non-being'),
                     ('Spirit', 'Spirit'))
    classification = models.CharField(max_length=6, choices=CLASS_CHOICES)
    RATING_CHOICES = ((0, 'Not Applicable'), (1,'X'),(2,'XX'),(3,'XXX'),(4,'XXXX'),(5,'XXXXX'))
    rating = models.IntegerField(default=0, choices=RATING_CHOICES, blank=True)
    image = models.ImageField(upload_to='images/')
    hidden = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def potions(self):
        return creature.ingredients.first().potions.all()

    def neutralize(self, incantation):
        return self.spells.first().incantation == incantation

    def get_absolute_url(self):
        return reverse('creature', args=[self.id]) 

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
    DIFFICULTY_CHOICES = (('Easy', 'Easy'),
                    ('Moderate', 'Moderate'),
                    ('Hard', 'Hard'),
                    ('Extremely Difficult', 'Extremely Difficult'))
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES)
    kind = models.CharField(max_length=20, choices=KIND_CHOICES)
    image = models.ImageField(upload_to='images/')

     # affects certain creatures
    creature = models.ForeignKey('Creature', blank=True, null=True, related_name='spells')

    def __str__(self):
        return self.incantation

    def get_absolute_url(self):
        return reverse('spell', args=[self.id]) 

class Ingredient(models.Model):
    name = models.CharField(max_length = 100)
    creature = models.ForeignKey('Creature', null=True, blank=True, related_name = 'ingredients')

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
    effects = models.TextField()
    recipe = models.TextField()
    notable_uses = models.TextField()
    physical_description = models.TextField()
    ingredients = models.ManyToManyField(Ingredient, related_name = 'potions', null=True, blank=True)
    image = models.ImageField(upload_to = 'images/', default = 'images/empty.jpg')

    def __str__(self):
        return self.title

    def brew(self, available_ingredients):
        for required in self.ingredients.all():
            if(not required.name in available_ingredients):
                return 'Failure'
        if(self.ingredients.all().count() == len(available_ingredients)):
            return 'Success'
        return 'Explosion!'

    def get_absolute_url(self):
        return reverse('potion', args=[self.id]) 

class Location(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    kind = models.CharField(max_length=20)
    image = models.ImageField(upload_to = 'images/', default = 'images/empty.jpg')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('location', args=[self.id]) 

class School(Location):
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('school', args=[self.id]) 

class House(School):
    school = models.ForeignKey(School, related_name = 'houses')
    ghost = models.ForeignKey(Character, related_name = 'houses_haunted')
    colors = models.CharField(max_length=100)
    mascot = models.CharField(max_length=100)
    quote = models.TextField()
    quote_by = models.CharField(max_length=100)
    founder = models.ForeignKey('Character', related_name = 'house_founded')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('house', args=[self.id]) 

class Shop(Location):
    locations = models.ManyToManyField(Location, related_name = 'shops', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('shop', args=[self.id]) 

class Artifact(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    kind = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='images/', default='images/empty.jpg')
    owners = models.ManyToManyField(Character, related_name = 'artifacts', blank=True, null=True)
    shop  = models.ForeignKey(Shop, related_name='artifacts', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('artifact', args=[self.id]) 

class Book(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(Character, related_name = 'books_published', blank=True, null=True)
    subjects = models.ManyToManyField(Character, null=True, blank=True, related_name='books_starred')
    publisher = models.CharField(max_length = 200, null=True, blank=True)
    published_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to = 'images/', default = 'images/empty.jpg')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book', args=[self.id]) 

class Story(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    book = models.ForeignKey(Book, related_name = 'story', null=True, blank=True)
    kind = models.CharField(max_length=20)
    characters = models.ManyToManyField('Character', related_name = 'stories')
    artifacts = models.ManyToManyField('Artifact', related_name = 'stories', null=True, blank=True)
    locations = models.ManyToManyField('Location', related_name = 'stories', null=True, blank=True)
    quote = models.TextField(null=True, blank=True)
    quote_by = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to = 'images/', default = 'images/empty.jpg')

    def century(self):
        return self.date.year // 100 + 1

    def __str__(self):
        return self.name

    def formatted_date(self):
        if(self.date.month == 1 and self.date.day == 1):
            if(self.date.year % 100 == 0):
                p = inflect.engine()
                return "%s Century" %(p.ordinal(self.century()))
            else:
                return self.date.year
        return self.date.strftime("%B %d, %Y")

    class Meta:
        verbose_name_plural = 'stories'

    def get_absolute_url(self):
        return reverse('story', args=[self.id]) 

class Relationship(models.Model):
    #relationships
    character1 = models.ForeignKey(Character, related_name = "relationships1", blank=True, null=True)
    character2 = models.ForeignKey(Character, related_name = "relationships2", blank=True, null=True)
    descriptor1 = models.CharField(max_length=100)
    descriptor2 = models.CharField(max_length=100)

    def __str__(self):
        return "%s (%s) -- %s (%s)" %(self.character1.name, self.descriptor1, self.character2.name, self.descriptor2)

