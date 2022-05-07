from django.conf.urls import url

from secondary import views

urlpatterns = [
     url('android/', views.secuser.as_view())
]
