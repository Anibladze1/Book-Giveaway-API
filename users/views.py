from django.contrib.auth import authenticate, login, logout, get_user_model
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterSerializer, LoginSerializer, DeleteUserSerializer, LogoutSerializer

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes


class RegisterAPIView(APIView):
    """
    API endpoint that allows new users to register.
    """
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(APIView):
    """
    API endpoint for user login.

    Authenticates the user using email and password and returns an access token.
    """
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data["password"]

            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                return Response({'access_token': access_token, 'refresh_token': str(refresh)},
                                status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@extend_schema(
    responses={200: LogoutSerializer}
)
class LogoutAPIView(APIView):
    serializer_class = DeleteUserSerializer
    """
    API endpoint for user logout.

    Ends the user's current session.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)


@extend_schema(
    parameters=[
        OpenApiParameter(name='user_id', description='ID of the user to be deleted', required=True, type=OpenApiTypes.INT)
    ],
    responses={200: DeleteUserSerializer}
)
class DeleteUserAPIView(APIView):
    """
    API endpoint to delete a user.

    Allows a user to delete their own account or lets a superuser delete any user account.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DeleteUserSerializer

    def delete(self, request, user_id=None):
        User = get_user_model()
        if request.user.id == user_id or request.user.is_superuser:
            try:
                user_to_delete = User.objects.get(id=user_id)
                user_to_delete.delete()
                return Response({'message': 'User deleted successfully'}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'Not allowed'}, status=status.HTTP_403_FORBIDDEN)
