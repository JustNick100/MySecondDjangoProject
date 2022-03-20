from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Agent)
admin.site.register(Service)
admin.site.register(Service_faq)
admin.site.register(Service_faq_docs)
admin.site.register(Service_faq_link)
admin.site.register(Transcript)
admin.site.register(Categories_suggestion)
admin.site.register(Category)
admin.site.register(Language)
admin.site.register(Client)
admin.site.register(Language_translations)


