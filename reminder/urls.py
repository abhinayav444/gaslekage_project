from django.conf.urls import url

from reminder import views

urlpatterns =[
    url('android/', views.rem.as_view()),
    url('android1/', views.editrem.as_view()),
    url('del/', views.deleterem.as_view())
]     