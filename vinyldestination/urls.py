from django.conf.urls import url
from django.urls import path
from django.urls import include
from vinyldestination import views

app_name = 'vinyldestination'
urlpatterns = [
    path('', views.index, name='index'),
    path('artists/', views.artists, name='artists'),
    path('records/', views.records, name='records'),
    path('records/<slug:record_name_slug>/', views.show_record,
        name='show_record'),
    path('records/<slug:record_name_slug>/add_review/', views.add_review,
        name='add_review'),
    path('artists/<slug:artist_name_slug>/', views.show_artist,
        name='show_artist'),
    path('register/', views.register, name='register'), 
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]

