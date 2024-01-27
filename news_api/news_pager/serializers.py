
from django.contrib.auth.models import Group, User
from rest_framework import serializers
from django.urls import reverse

from .models import *



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['login', 'password']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['mark_news_id', 'user_id']

class RegistrSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ['login', 'password']

class AuthSerializer(serializers.ModelSerializer):
    mark_news = ProfileSerializer()

    class Meta:
        model = Users
        fields = ['login', 'password', 'mark_news']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']

class NewsSerializer(serializers.ModelSerializer):
    category = CategorySerializer(source='category_id', read_only=True)  # Указываем source и read_only
    image_url = serializers.SerializerMethodField()
    #image = serializers.ImageField(source='image.url', read_only=True)
    class Meta:
        model = News
        fields = ['title', 'text', 'date','image','image_url', 'category']

    def get_image_url(self, obj):
        # Возвращаем URL изображения, если оно существует
        if obj.image:
            request = self.context.get('request')
            if request is not None:
                return request.build_absolute_uri(reverse('get_news_image', args=[obj.pk]))
        return None

