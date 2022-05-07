from django.conf.urls import url

from temp import views

urlpatterns = [

    url('authority_home/', views.authority_home),
    url('mainhome/', views.mainhome)
]