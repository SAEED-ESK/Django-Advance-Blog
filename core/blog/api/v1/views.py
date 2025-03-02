from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import mixins
from rest_framework import viewsets 
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import get_object_or_404
from .serializers import PostSerializer, CategorySerializer
from ...models import Post, Category
from .permissions import IsAuthorOrReadOnly
from .paginations import DefaultPagination

class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    pagination_class = DefaultPagination
    filterset_fields = {'author': ['exact'], 'category': ['exact', 'in']}
    search_fields = ['title', 'content']
    ordering_fields = ['published_date']


# class PostViewSet(viewsets.ViewSet):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()

#     def list(self, request):
#         serializer = self.serializer_class(self.queryset, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         post_object = get_object_or_404(self.queryset, pk=pk)
#         serializer = self.serializer_class(post_object)
#         return Response(serializer.data)

#     def update(self, request, pk=None):
#         post_object = get_object_or_404(self.queryset, pk=pk)
#         serializer = self.serializer_class(post_object, data=request.data)
#         serializer.is_valid()
#         serializer.save()
#         return Response(serializer.data)
    
#     def destroy(self, request, pk=None):
#         post_object = get_object_or_404(self.queryset, pk=pk)
#         post_object.delete()
#         return Response({'detail': 'Post deleted'}, status=status.HTTP_204_NO_CONTENT)




'''@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def postListApi(request):
    if request.method == 'GET':
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)'''

'''class PostListApi(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)'''

class PostListApi(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()



'''@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def postDetailApi(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response({'detail': 'Post deleted'}, status=status.HTTP_204_NO_CONTENT)'''

'''
class PostDetailApi(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request, id):
        post = get_object_or_404(Post, pk=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def put(self,request, id):
        post = get_object_or_404(Post, pk=id)
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self,request, id):
        post = get_object_or_404(Post, pk=id)
        post.delete()
        return Response({'detail': 'Post deleted'}, status=status.HTTP_204_NO_CONTENT)
'''

class PostDetailApi(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = queryset = Post.objects.all()
