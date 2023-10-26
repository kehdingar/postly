from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Vote
from .serializers import VoteSerializer

class VoteView(APIView):
    def post(self, request):
        # serializer = VoteSerializer(data=request.data)
        serializer = VoteSerializer(data=request.data, context={'request': self.request})

        if serializer.is_valid():
            post = serializer.validated_data['post']
            value = serializer.validated_data['value']
            instance = serializer.save()
            if value == 1:
                post.upvote()
            elif value == -1:
                post.downvote()
            # added id so that it can be used with tests
            return Response({"id": instance.id,'data':serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)