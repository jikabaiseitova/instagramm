from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

from .models import Post, Comment
from .permissions import PostPermission
from .serializers import PostSerializer, CommentSerializer


@api_view(http_method_names=['GET', 'POST'])
@authentication_classes([TokenAuthentication, ])
@permission_classes([PostPermission, ])
def post_list_create_api_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        user = request.user
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#
# @api_view(http_method_names=['GET', 'PUT', 'DELETE'])
# @authentication_classes([TokenAuthentication, ])
# @permission_classes([IsAuthenticated, IsAuthor])
# def post_retrieve_update_destroy_api_view(request, pk):
#     if request.method == 'GET':
#         post = Post.objects.get(id=pk)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)
#     if request.method == 'PUT':
#         user = request.user
#         post = Post.objects.get(id=pk)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#


class PostRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [PostPermission]


class CommentListCreateAPIView(ListCreateAPIView):
    """
    Класс Для получения информации о комментариях к посту
    """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [PostPermission]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [PostPermission]

