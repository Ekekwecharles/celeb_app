from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_celebrities, name='show_celebrities'),
    path('vote/', views.vote_celebrity, name='vote_celebrity'),
    path('enter_token/', views.enter_token, name='enter_token'),
]