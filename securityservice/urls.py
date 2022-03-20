from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',include('chatbot.urls')),
    path('adminpanel/',include('adminpanel.urls')),

    path('', include('admin_panel_api.urls')),
]
