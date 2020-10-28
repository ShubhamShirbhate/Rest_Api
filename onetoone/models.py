from django.db import models


class PostRates(models.Model):
    likes = models.BigIntegerField(default=0)
    dislikes = models.BigIntegerField(default=0)


class Post(models.Model):
    post_title = models.CharField(max_length=20)
    post_body = models.TextField()
    rates = models.OneToOneField(PostRates, on_delete=models.CASCADE)


    def __str__(self):
        return self.post_title

