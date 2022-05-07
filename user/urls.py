from django.conf.urls import url

from user import views

urlpatterns = [
    url('android/',views.user.as_view()),
    url('android1/',views.user_addloc.as_view())

]
