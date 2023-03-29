from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, UpdateView, DeleteView)

from .filters import PostFilter
from .models import Post, Response
from .forms import PostForm, RespForm, AcceptForm


class PostList(ListView):
    model = Post
    ordering = '-date'
    template_name = 'board/board.html'
    context_object_name = 'board'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.request.user
        return context


class AdvertList(DetailView):
    model = Post
    template_name = 'board/advert.html'
    context_object_name = 'advert'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.request.user
        return context


class ResponseList(ListView):
    model = Response
    ordering = 'post'
    template_name = 'board/response.html'
    context_object_name = 'response'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        context['author'] = self.request.user
        return context


@login_required
def post_add(request):
    form = PostForm()

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect(post_add)

    return render(request, 'board/create.html', {
        'form': form
    })


@login_required
def resp_add(request, pk):
    form = RespForm()
    posts = Post.objects.get(id=pk)

    if request.method == "POST":
        form = RespForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.post = posts
            post.save()
            return redirect('board')

    return render(request, 'board/resp_create.html', {
        'form': form
    })


class PostUpdate(LoginRequiredMixin, UpdateView):
    permission_required = ('news.change_news',)
    form_class = PostForm
    model = Post
    template_name = 'board/post_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.request.user
        return context


class PostDelete(LoginRequiredMixin, DeleteView):
    permission_required = ('news.delete_news',)
    model = Post
    template_name = 'board/post_delete.html'
    success_url = reverse_lazy('board')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.request.user
        return context


class RespUpdate(LoginRequiredMixin, UpdateView):
    permission_required = ('resp_up',)
    form_class = AcceptForm
    model = Response
    template_name = 'board/resp_update.html'
    success_url = reverse_lazy('response')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.request.user
        return context


class RespDelete(LoginRequiredMixin, DeleteView):
    permission_required = ('resp_delete',)
    model = Response
    template_name = 'board/resp_delete.html'
    success_url = reverse_lazy('response')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author'] = self.request.user
        return context

