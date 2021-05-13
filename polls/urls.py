from django.conf.urls import url
from . import views

app_name = "polls"

urlpatterns = [
    url(r'myhome',views.myhome, name='myhome'),
    url(r'^add$',views.add,name='addition')
]
