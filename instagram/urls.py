from django.contrib.auth import views 
urlpatterns = [
#....
    url(r'^logout/$', views.logout, {"next_page": '/'}), 
] 