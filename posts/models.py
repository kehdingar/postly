from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    score = models.IntegerField(default=0)

    class Meta:
        ordering = ['-score']

    def upvote(self):
        self.score += 1
        self.save()
        print(f"UPVOTED... {self.score}")

    def downvote(self):
        self.score -= 1
        print("DOWNVOTED...")        
        self.save()

    def __str__(self):
        return self.title

class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # This will prevent users from liking a post twice
        unique_together = ('post', 'user')

    def __str__(self):
        return f'{self.user.username} likes {self.post.title}'
