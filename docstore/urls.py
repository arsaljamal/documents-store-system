from django.urls import re_path, include
from docstore import views

urlpatterns = [
    re_path(r'^api/folders', views.folders_list),
    re_path(r'^api/folder/(?P<pk>[0-9]+)$', views.folders_detail),
    re_path(r'^api/documents', views.documents_list),
    re_path(r'^api/document/(?P<pk>[0-9]+)$', views.documents_detail),
    re_path(r'^api/topics', views.topics_list),
    re_path(r'^api/topic/(?P<pk>[0-9]+)$', views.topics_detail),
    re_path(r'^api/search', views.documents_list)
]