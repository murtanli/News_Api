from rest_framework import permissions

class MyCustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET' and request.user.is_authenticated:
            return True  # Разрешение GET запросов для всех пользователей
        elif request.method == 'POST' and request.user.is_authenticated:
            return True  # Разрешение POST запросов для авторизованных пользователей
        return False