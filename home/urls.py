from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home')
]
from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns
    path('profile/', views.profile_view, name='profile'),
]
