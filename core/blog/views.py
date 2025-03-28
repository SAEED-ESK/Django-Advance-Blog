from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import PostForm


# Create your views here.
# def indexView(request):
#     title = "Function BV"
#     context = {"title": title}
#     return render(request, "index.html", context)


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        content = super().get_context_data(**kwargs)
        content["title"] = "Class BV"
        return content


class PostListView(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 2


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ["title", "content", "status", "category", "published_date"]
    success_url = "/blog/posts/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostEditView(UpdateView):
    model = Post
    form_class = PostForm
    success_url = "/blog/posts/"


class PostDeleteView(DeleteView):
    model = Post
    success_url = "/blog/posts/"
