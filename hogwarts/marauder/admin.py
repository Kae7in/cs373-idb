from django.contrib import admin
from django.db.models import get_models, get_app

# Register your models here.
for model in get_models(get_app('marauder')):
    admin.site.register(model)
