from django.shortcuts import render
from .models import Articles
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy


# Create your views here.
class ArticleListView(ListView):
    context_object_name = 'acticle'
    model = Articles
    template_name = 'article_list.html '


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Articles
    template_name = 'article_detail.html'
    login_url = 'login'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Articles
    fields = ('title', 'kichik', 'body', 'photo')
    template_name = 'article_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Articles
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Articles
    template_name = 'article_new.html'
    fields = ('title', 'kichik','body', 'photo',)
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
