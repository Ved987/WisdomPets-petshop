from django.contrib import admin
from django.urls import path

from adoptions import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='Home'),
    path('adoptions/<int:pet_id>/', views.pet_details, name='pet_detail'),
]

