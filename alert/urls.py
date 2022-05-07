from django.conf.urls import url

from alert import views

urlpatterns=[
    url('view_alert/', views.view),
    url('android1/', views.alertstatus.as_view()),
    url('android/', views.alertt.as_view()),
]
