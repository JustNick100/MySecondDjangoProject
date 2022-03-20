from django.urls import path, include

from .views import *

app_name='adminpanel'

urlpatterns = [
    path('users/',users,name="users"),
    path('agents/',agents,name="agents"),
    path('categories/',categories,name="categories"),
    path('categories_suggestions/',categories_suggestions,name="categories_suggestions"),
    path('transcripts/',transcripts,name="transcripts"),
    path('transcripts_messages/',transcripts_messages,name="transcripts_messages"),
    path('clients/',clients,name="clients"),
    path('languages/',languages,name="languages"),
    path('language_translations/',language_translations,name="language_translations"),
    path('services/',services,name="services"),
]
