from django.contrib.auth import views 
urlpatterns = [
#....
    url(r'^logout/$', views.logout, {"next_page": '/'}), 
     url(r'^new/detail$', views.new_detail, name='new-detail')
] 