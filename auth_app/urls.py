from django.urls import conf, path ,include
from . import views

app_name='auth_app'
urlpatterns = [
    path('',views.home , name='routejid3'),
    path('home/',views.home , name='home'),
    path('settings/',views.settings , name='settings'),
    path('traffic/',views.traffic , name='traffic'),

    #path('test',views.test , name='test'),
]