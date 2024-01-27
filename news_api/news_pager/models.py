from django.db import models

class Users(models.Model):
    login = models.CharField(max_length = 20)
    password = models.CharField(max_length = 20)

class Category(models.Model):
    category = models.CharField(max_length = 20)

class News(models.Model):
    title = models.CharField(max_length = 40)
    text = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='news_images/', blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)

class Profile(models.Model):
    mark_news_id = models.ManyToManyField(News, related_name='bookmarked_by')
    user_id = models.ForeignKey(Users, on_delete = models.CASCADE)
