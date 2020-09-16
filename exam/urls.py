from exam import views
from django.conf.urls import url  # imported


urlpatterns = [

    url('test',views.showTest),
    url('result',views.showResult),
 

] 