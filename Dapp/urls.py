from django.urls import path
from Dapp.views import HomeView

urlpatterns = [path('', HomeView.as_view(), name='home')]