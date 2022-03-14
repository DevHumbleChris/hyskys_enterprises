from django.urls import path
from .views import HomeView

app_name = 'hyskys'

urlpatterns = [
    path('', HomeView, name='home')
]
