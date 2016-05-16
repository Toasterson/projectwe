from django.conf.urls import url

from . import views

app_name = "projectwe"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'projects$', views.ListView.as_view(), name='list'),
    url(r'^project/(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),
    url(r'^project/upload', views.UploadProjectView.as_view(), name='create_project'),
]