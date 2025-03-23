from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'api/v1'

router = DefaultRouter()
router.register("post", views.PostViewSet, basename="post")
router.register("category", views.CategoryViewSet, basename="category")

urlpatterns = router.urls

# urlpatterns = [
#     # path('post', views.postListApi, name='post-list'),
#     # path('post', views.PostListApi.as_view(), name='post-list'),
#     # path('post/<int:id>/', views.postDetailApi, name='api-post-detail'),
#     # path('post/<int:pk>/', views.PostDetailApi.as_view(), name='api-post-detail'),
#     path('post', views.PostViewSet.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
#     path('post/<int:pk>/', views.PostViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='post-detail'),
# ]
