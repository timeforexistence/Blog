from django.contrib import admin
from django.urls import path
from blogengine.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('<str:slug>/', PostDetailView.as_view(), name='detailed_post'),
    path('', PostListView.as_view(), name='post_list'),
    #path('tags???', )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)