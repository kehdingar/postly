from rest_framework import serializers
from .models import Vote
from django.core.validators import MaxValueValidator, MinValueValidator


class VoteSerializer(serializers.ModelSerializer):
    # Inbuilt validation takes precedence over custom validate()
    value = serializers.IntegerField(
        validators=[
            MaxValueValidator(1, message='Invalid vote, Vote has has to be less than 1.'),
            MinValueValidator(-1, message='Value cannot be negative.')
        ],
        error_messages={
            'required': 'Please provide a value.',
            'invalid': 'Invalid value. Please provide a valid integer.'
        }
    )
    class Meta:
        model = Vote
        fields = ['id', 'user', 'post', 'value']
        read_only_fields = ['id', 'user']
    
    def save(self, **kwargs):
        user = self.context['request'].user
        validated_data = dict(self.validated_data, user=user)
        vote = Vote.objects.create(**validated_data)
        return vote    

    def validate(self, data):
        post = data['post']
        # use the current user from the request object        
        user = self.context['request'].user
        value = data['value']
        print(f"HERE IS THE VALUE {value}")
        if value not in [-1, 0, 1]:
            print("Custom ERROR.......")
            raise serializers.ValidationError('Invalid vote value.')
        if Vote.objects.filter(post=post, user=user).exists():
            raise serializers.ValidationError('You have already voted on this post.')
        return data