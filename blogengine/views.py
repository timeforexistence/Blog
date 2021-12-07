from django.shortcuts import render
from django.http import HttpResponse
from blogengine.utils import *
from django.views.generic import ListView, DetailView
from django.views import View
from blogengine.models import *


#def index(request):
#    posts = Post.objects.order_by('-pub_date')
#    context = {
#        'posts': posts,
#        'title': 'Список постов'
#    }
#    return render(request, template_name='blogengine/index.html', context=context)

class PostListView(ListView):
    model = Post
    template_name = 'blogengine/post_list.html'


class PostDetailView(DetailObjectMixin, View):
    model = Post
    template = 'blogengine/detailed_post.html'


# Откладываем в сторону, разбираемся с миксинами
#class PostDetailView(DetailView):
#    model = Post
#    template_name = 'blogengine/detailed_post.html'