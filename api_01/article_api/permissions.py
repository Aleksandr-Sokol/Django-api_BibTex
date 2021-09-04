from rest_framework import permissions


class MyPermissions(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.user.is_authenticated:
            return True # пользователь аутентифицирован
        return False # пользователь неаутентифицирован

    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return False