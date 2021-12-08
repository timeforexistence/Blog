from django.shortcuts import render
from django.http import HttpResponse
from blogengine.utils import *
from django.views.generic import ListView, DetailView
from django.views import View
from blogengine.models import *


class PostListView(ListView):
    # class ListView allow use pagination
    paginate_by = 5
    model = Post
    template_name = 'blogengine/post_list.html'


class PostDetailView(DetailObjectMixin, View):
    model = Post
    template = 'blogengine/detailed_post.html'


class TagListView(ListView):
    model = Tag
    template = 'blogengine/detailed_tags.html'


class TagDetailView(DetailObjectMixin, View):
    model = Tag
    template = 'blogengine/detailed_tags.html'

