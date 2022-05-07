from django.conf.urls import url

from authority import views

urlpatterns = [
    url('contactinfo/', views.info),
    url('reg/',views.reg)

]