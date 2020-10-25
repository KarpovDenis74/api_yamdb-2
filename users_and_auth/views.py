from .models import User
from .serializer import UserSerializer, UserEditSerializer
from .permissions import Permission1
from django.shortcuts import get_object_or_404
from rest_framework.permissions import (
    IsAuthenticated)
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view
from .pagination import CustomPagination
from rest_framework import status
from django.core.mail import send_mail
import random
from rest_framework.decorators import action
from django.conf import settings


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, Permission1]
    pagination_class = CustomPagination
    lookup_field = 'username'

    @action(detail=False, methods=['GET'], url_path='me', permission_classes=[IsAuthenticated])
    def get(self, request):
        user = request.user
        serializer = UserSerializer(user, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['PATCH'], url_path='me')
    def patch(self, request):
        permission_classes = [IsAuthenticated]
        user = request.user
        serializer = UserEditSerializer(
            user, data=request.data, many=False, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_403_FORBIDDEN)

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

@api_view(('POST',))
def token(request):
    email = request.data.get('email')
    confirmation_code = request.data.get('confirmation_code')
    user = get_object_or_404(
        User, email=email)
    tokens = get_tokens_for_user(user)
    return Response({"message": tokens})

@api_view(('POST',))
def reg_user_email(request):
    if not request.data.get('email'):
        return Response({'message': {
            'Ошибка': 'Не указана почта для регистрации'}},
             status=status.HTTP_403_FORBIDDEN)
    try:
        email = request.data.get('email')
        confirmation_code = random.randint(1, 100000000)
        a, b = get_user_model().objects.get_or_create(
            email=email, defaults={'confirmation_code': confirmation_code})
    except:
        return Response({'message': {
            'Ошибка': 'Ошибка запроса'}}, status=status.HTTP_403_FORBIDDEN)
    send_mail(
        'Подтверждение адреса электронной почты YaTube',
        'Вы получили это письмо, потому что регистрируетесь на ресурсе '
        'YaTube Код подтверждения confirmation_code=' + str(confirmation_code),
        settings.DEFAULT_FROM_EMAIL,
        [email,],
        fail_silently=False,)
    return Response({'message': {
        'ОК': f'Пользователь c email {email} создан успешно. '
        'Код подтверждения отправлен на электронную почту'}})
