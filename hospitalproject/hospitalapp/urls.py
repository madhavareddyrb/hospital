from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include


urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', include('hospitalapp.urls')),
    path('', views.home, name='home'),

]