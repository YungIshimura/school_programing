from django.contrib import admin
from django.urls import path
from .views import view_index, view_sign_in, view_registration


app_name = 'school'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_index, name='index'),
    path('sign-in/', view_sign_in, name='sign-in'),
    path('registration/', view_registration, name='registration')
]
