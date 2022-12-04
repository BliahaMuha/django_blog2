from django.shortcuts import render
from django.views import View
from .models import Post
from django.core.paginator import Paginator

class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request,
        'home.html'
        )

class MainView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        paginator = Paginator(posts, 6)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'home.html', context={
            'page_obj': page_obj
        })
# Create your views here.
""" class MainView(View):
    def get(self,request,*args, **kwargs):
        posts = Post.objects.all() """
