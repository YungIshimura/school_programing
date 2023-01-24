from django.contrib import admin
from django.urls import path
from .views import view_index


app_name = 'school'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_index, name='index')
]
