from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes

from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, BasePermission


class IsAdminPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.username.startswith('adm'):
            return True
        return False


@api_view(http_method_names=['GET',])
def who_am_i(request):
    # print(request.auth)     #None
    # print(request.user)     #AnonymusUser
    user = request.user
    data = {
        'login': user.username,
        'email': user.email
    }
    return Response(data)


@api_view(http_method_names=['GET', ])
@authentication_classes(authentication_classes=[BasicAuthentication, ])
@permission_classes([IsAdminPermission, ])
def basic_view(request):
    user = request.user
    return Response(user.username)


@api_view(http_method_names=['GET', ])
@authentication_classes(authentication_classes=[TokenAuthentication, ])
@permission_classes([IsAdminPermission, ])
def token_view(request):
    user = request.user
    return Response(user.email)

