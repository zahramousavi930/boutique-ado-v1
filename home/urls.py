from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home')
]


urlpatterns = [
    # Other URL patterns
    path('profile/', views.profile_view, name='profile'),
    path('', views.index, name='home'),
]
