from django.conf.urls import url, include
from django.views.generic.base import TemplateView

from . import views

app_name = "projectwe"
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'projects$', views.ListView.as_view(), name='list'),
    url(r'^project/(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail'),
    url(r'^project/(?P<pk>[0-9]+)/members$', views.MembersView.as_view(), name='members'),
    url(r'^project/edit/(?P<pk>[0-9]+)$', views.EditProjectView.as_view(), name='edit'),
    url(r'^project/upload', views.UploadProjectView.as_view(), name='create_project'),
    url(r'^project/(?P<pk>[0-9]+)/join', views.join_project, name='join_project'),
    url(r'^project/(?P<pk>[0-9]+)/leave', views.leave_project, name='leave_project'),
    url(r'^user/(\w+)/$', views.profile, name='profile'),
    url(r'^user/(\w+)/edit$', views.ProfileEditView.as_view(), name='profile_edit'),
    url(r'', include('registration.backends.simple.urls')),
    url(r'', include('registration.auth_urls')),
]
