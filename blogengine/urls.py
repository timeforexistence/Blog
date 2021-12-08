from django.contrib import admin
from django.urls import path
from blogengine.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('post/<str:slug>/', PostDetailView.as_view(), name='detailed_post'),
    path('', PostListView.as_view(), name='post_list'),
    path('tag/<str:slug>/', TagDetailView.as_view(), name='detailed_tags'),
    path('tag_list/', TagListView.as_view(), name='tag_list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


