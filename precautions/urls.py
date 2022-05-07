from django.conf.urls import url

from precautions import views

urlpatterns = [
    url('precautions_authority/', views.preca),
    url('android/', views.prec_view.as_view())

]