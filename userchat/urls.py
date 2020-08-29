
from django.conf.urls import url
from . import views



app_name ='userchat'

urlpatterns= [
url(r'^$',views.login , name ='login') ,
url(r'^login$',views.login , name ='login') ,
url(r'^register$',views.register , name ='register') ,
url(r'^welcome$',views.welcome , name ='welcome') ,
url(r'^addfriend$',views.addfriend, name ='addfriend') ,
url(r'^showProfile$',views.showProfile, name ='showProfile') ,
url(r'^modifyP$', views.modifyP, name ='modifyP') ,
url(r'^ajax/check_email_field$', views.ajax_check_email_field, name ='ajax_check_email_field') ,

]
