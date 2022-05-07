from django.conf.urls import url

from login import views

urlpatterns = [
    url('login/', views.log),
    url('android/', views.log_view.as_view()),

]