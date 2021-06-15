from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView

from .models import *

class NewsList(ListView):
    paginate_by = 2
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'

class NewsDetail(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'

class Search(ListView):
    paginate_by = 2
    model = Post
    template_name = 'search.html'
    context_object_name = 'news'
    def get_queryset(self):
        qs = super().get_queryset()
        search = self.request.GET.get('search', None)
        ordering = self.request.GET.getlist('ordering', None)
        if search: 
            qs = qs.filter(title = search)
        if ordering:
            for order in ordering:
                qs = qs.order_by(order)
        return qs
        
class NewsCreate(CreateView):
    model = Post
    template_name = 'create.html'
    fields = ['type', 'text', 'title', 'categories']
    success_url = '/news'
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user.author
        obj.save()
        return obj

class NewsEdit(UpdateView):
    model = Post
    template_name = 'edit.html'
    fields = ['title', 'text']
    success_url = '/news'

class NewsDelete(DeleteView):
    model = Post
    template_name = 'delete.html'

    success_url = '/news'