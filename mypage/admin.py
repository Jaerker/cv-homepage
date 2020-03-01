from django.contrib import admin
from . import models as mpModels
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
'''
Varje ny Model du har i models.py måste registreras här om man ska kunna komma åt 
tabellen på admin sidan. Det man lägger till är: 
admin.site.register(Achievement) (där Achievement självklar är själva model klassen)

Ovanför registreringen så har jag gjort ett eget upplägg för hur den ska se ut när man ändrar eller lägger till i modellen. 

Jag tar då bort tidsstämpeln just pga att jag inte behöver korrigera den, utan den är inställd i förväg på tiden som den blir skapad.
'''

class AchievementAdmin(admin.ModelAdmin):
    fields = ["achievement_name", 
              "achievement_description",]

class CodeExampleAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()}
    }

admin.site.register(mpModels.Achievement, AchievementAdmin)
admin.site.register(mpModels.CodeExample, CodeExampleAdmin)
admin.site.register(mpModels.IndexInfo)