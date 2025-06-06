from django.urls import path
from . import views

urlpatterns= [
  path('', views.home, name='home'),
  path('getMessages/<str:room>/', views.getMessages, name= "getMessages"),
  path('checkview', views.checkview, name='checkview'),
  path('send', views.send, name='send'),
     # finally the catch‑all room
  path('<str:room>/', views.room, name='room'),
]