from django.forms import ValidationError
from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Before saving add the author field which has been made readonly in serializer
    def perform_create(self,serializer):
        serializer.save(author=self.request.user)

    def destroy(self,request, *args, **kwargs):
        # post = self.get_object()
        try:
            post  = Post.objects.get(pk=kwargs['pk'])
            if post.author == request.user:
                self.perform_destroy(post)
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'error': 'You can only delete posts you create'}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({'error': 'Post does not exists'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['put'])
    def custom_update(self,request, *args, **kwargs):
        try:
            post  = Post.objects.get(pk=kwargs['pk'])
            if post.author == request.user:
                self.perform_update(post)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response({'error': 'You can only update posts you create'}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({'error': 'Post does not exists'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['patch'])
    def custom_patch(self,request, *args, **kwargs):
        try:
            post  = Post.objects.get(pk=kwargs['pk'])
            if post.author == request.user:
                self.partial_update(post)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response({'error': 'You can only update posts you create'}, status=status.HTTP_403_FORBIDDEN)
        except Exception as e:
            return Response({'error': 'Post does not exists'}, status=status.HTTP_404_NOT_FOUND)
        
    # This like action is placed here for convinience and consistency sice like is associated with posts
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user
        like = Like.objects.filter(post=post, user=user).first()
        if like:
            like.delete()
            return Response({'detail': 'Post unliked.'}, status=status.HTTP_200_OK)
        else:
            Like.objects.create(post=post, user=user)
            return Response({'detail': 'Post liked.'}, status=status.HTTP_201_CREATED)


class LikeAPIView(generics.ListAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        post_id = self.kwargs['pk']
        return Like.objects.filter(post=post_id)