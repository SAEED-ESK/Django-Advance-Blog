from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('fbv', views.indexView, name='fdv-test'),
    #path('cbv', TemplateView.as_view(template_name='index.html')),
    path('cbv', views.IndexView.as_view(), name='cbv'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/create/', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/edit/', views.PostEditView.as_view(), name='post-edit'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('api/v1/', include('blog.api.v1.urls')),
]