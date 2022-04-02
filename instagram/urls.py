from django.contrib.auth import views 
urlpatterns = [
#....
    url(r'^logout/$', views.logout, {"next_page": '/'}), 
     url(r'^accounts/', include('registration.backends.simple.urls')),
] 