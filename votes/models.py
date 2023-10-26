from django.db import models

from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator


User = get_user_model()

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    value = models.IntegerField(validators=[MaxValueValidator(1), MinValueValidator(-1)])

    class Meta:
        unique_together = ('user', 'post')
    
    def __str__(self):
        return f'{self.user.username} voted {self.value} on {self.post.title}'

