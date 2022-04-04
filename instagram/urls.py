from django.contrib.auth import views 
from django.urls import path
from . import views
urlpatterns = [
#....
    # path(r'^logout/$', views.logout, {"next_page": '/'}), 
    # path(r'^new/detail$', views.new_detail, name='new-detail'),
    path('',views.home,name='home'),
    path('register/',views.register,name='register'),

] 