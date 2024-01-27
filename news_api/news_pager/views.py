from django.http import FileResponse
from django.shortcuts import render
from rest_framework.generics import get_object_or_404

from .models import *
from .serializers import *
from rest_framework import permissions, viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class Registration_new_user(APIView):
    def post(self, request):
        serializer = RegistrSerializer(data=request.data)
        if serializer.is_valid():
            login = serializer.validated_data['login']
            password = serializer.validated_data['password']

            if Users.objects.filter(login=login).exists():
                return Response({"message": "Пользователь с таким логином уже существует"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                try:
                    user = Users(login=login, password=password)
                    user.save()

                    profile = Profile.objects.create(user_id=user)

                    news_ids = request.data.get('news_ids', [])

                    for news_id in news_ids:
                        news = News.objects.get(id=news_id)
                        profile.mark_news_id.add(news)
                except:
                    user.delete()
                    return Response({"message": "Системная ошибка"}, status=status.HTTP_400_BAD_REQUEST)

                return Response({"message": "Регистрация прошла успешно"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Ошибка в заполнении"}, status=status.HTTP_400_BAD_REQUEST)


class Authentication_new_user(APIView):
    def get(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            login = serializer.validated_data['login']
            password = serializer.validated_data['password']

            if not login or not password:
                return Response({"message": "Логин и пароль обязательны"}, status=status.HTTP_400_BAD_REQUEST)

            try:
                user = Users.objects.get(login=login)
                profile = Profile.objects.filter(user_id=user.pk).first()
            except Users.DoesNotExist:
                return Response({"message": "Пользователь не найден"}, status=status.HTTP_404_NOT_FOUND)

            if profile and password == user.password:
                serializer = ProfileSerializer(profile)
                return Response({"message": "Авторизация успешна", "user_data": serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Неправильный пароль или профиль не найден"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class Get_all_news(APIView):
    def get(self, request):
        news = News.objects.all()
        serializer = NewsSerializer(news, many=True, context={'request': request})

        # Добавляем 'id' в каждый объект новости
        serialized_data = []
        for idx, data in enumerate(serializer.data):
            data['id'] = news[idx].pk
            serialized_data.append(data)

        return Response({"news": serialized_data}, status=status.HTTP_200_OK)

class Get_all_category(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response({"categoryes": serializer.data})

def get_news_image(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    # Путь к изображению в MEDIA_ROOT
    image_path = news.image.path
    # Отправляем файл в ответе
    return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')


class Save_marked_news(APIView):
    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            user_id = serializer.validated_data['user_id']
            marked_news = serializer.validated_data['mark_news_id']

            try:
                profile = Profile.objects.get(user_id=user_id)
            except Profile.DoesNotExist:
                return Response({"message": "Профиль не найден"}, status=status.HTTP_404_NOT_FOUND)

            # Очистим текущие закрепленные новости и добавим новые
            profile.mark_news_id.clear()
            profile.mark_news_id.add(*marked_news)

            return Response({"message": "Закрепленные новости обновлены"}, status=status.HTTP_200_OK)

        return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class Get_news_cat(APIView):
    def post(self, request):
        serializer = CategorySerializer(data=request.data)

        if serializer.is_valid():
            category = serializer.validated_data['category']
            news = News.objects.filter(category_id__category=category)
            serialized_data = []

            # Создаем экземпляр NewsSerializer для каждой новости
            for data in news:
                news_serializer = NewsSerializer(data, context={'request': request})
                data_dict = news_serializer.data
                data_dict['id'] = data.pk
                serialized_data.append(data_dict)

            return Response({"news": serialized_data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



