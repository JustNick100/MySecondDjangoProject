from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Language)
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(ChatTracker)
admin.site.register(Intent)
