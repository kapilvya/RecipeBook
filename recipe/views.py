from typing import Optional
from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import (LoginRequiredMixin ,
                                        UserPassesTestMixin)
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)





def home(request):
    context={      
        # 'posts':posts        #assigning dictionary to variavble posts
        'posts' : Post.objects.all()
        }
    
    return render(request,'recipe/home.html',context)

    
# if request.GET.get('search'):
#     model=model.filter(Post.title__icontains) 

class PostListView(ListView):
    model = Post
    # <app>/<model>_<viewtype>.html
    template_name = 'recipe/home.html'
    context_object_name='posts'
    ordering=['-date_posted']   #newest post coming at top
    
      
    
            

class PostDetailView(DetailView):
    model = Post
    
class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields=['title' , 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields=['title' , 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self) :
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False   #it will give 403 forbidden

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url='/'
    
    def test_func(self) :
        post=self.get_object()
        if self.request.user == post.author:
            return True
        return False   #it will give 403 forbidden


def about(request):

    return render(request,'recipe/about.html',{'title':'About'})

