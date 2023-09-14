# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth import login, logout
# from .serializers import UserSerializer, LoginSerializer , UserUpdateSerializer
# from .models import CustomUser
# from rest_framework.authtoken.models import Token
# from rest_framework_simplejwt.tokens import RefreshToken

# class SignupView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class LoginView(APIView):
#     def post(self, request):
#         serializer = LoginSerializer(data=request.data, context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         login(request, user)
#         return Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)

# class LogoutView(APIView):
#     def post(self, request):
#         logout(request)
#         return Response({'message': 'Logout successful.'}, status=status.HTTP_200_OK)
    

# class UserListAPIView(APIView):
#     def get(self, request):
#         users = CustomUser.objects.all()
#         serializer = UserSerializer(users, many=True)
#         return Response(serializer.data)
    

# class UserDetailAPIView(APIView):
#     def get(self, request, pk):
#         try:
#             user = CustomUser.objects.get(pk=pk)
#         except CustomUser.DoesNotExist:
#             return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = UserSerializer(user)
#         return Response(serializer.data)

#     def put(self, request, pk):
#         try:
#             user = CustomUser.objects.get(pk=pk)
#         except CustomUser.DoesNotExist:
#             return Response({'message': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = UserUpdateSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def logout_user(request):
#         if request.method == "POST":
#             request.user.auth_token.delete()
#         return Response({"Message": "You are logged out"}, status=status.HTTP_200_OK)
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from .models import CustomUser, Teacher
from .serializers import CustomUserSerializer, TeacherSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrAdmin, IsAdminOrSchool, IsTeacher
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def ngo_signup(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response({'message': 'NGO user created successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminOrSchool])
def ngo_logout(request):
    logout(request)
    return Response({'message': 'NGO user logged out successfully'}, status=status.HTTP_200_OK)

class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminOrReadOnly]

class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminOrReadOnly]

class HealthworkerList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdminOrReadOnly]

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsOwnerOrAdmin])
def healthworker_detail(request, pk):
    try:
        healthworker = Teacher.objects.get(pk=pk)
    except Teacher.DoesNotExist:
        return Response({'message': 'Health worker not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TeacherSerializer(teacher)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = TeacherSerializer(teacher, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        healthworker.delete()
        return Response({'message': 'Health worker deleted'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAdminOrSchool])
def healthworker_signup(request):
    serializer = TeacherSerializer(data=request.data)
    if serializer.is_valid():
        password = request.data.get('password')  
        hashed_password = make_password(password)
        healthworker = serializer.save(password=hashed_password)

        creator_id = request.data.get('created_by')
        if creator_id:
            creator = CustomUser.objects.filter(id=creator_id).first()
            if creator:
                healthworker.created_by = creator
                healthworker.save()
        return Response({'message': 'Health worker registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminOrSchool])
def healthworker_logout(request):
    logout(request)
    return Response({'message': 'Health worker logged out successfully'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsTeacher])
def healthworker_login(request):
    phone_number = request.data.get('phone_number')
    password = request.data.get('password')
    user = Teacher.objects.filter(phone_number=phone_number).first()
    print(f"<<<<<<<<<<<<<<<<<<<<<<<<<<<{user}>>>>>>>>>>>>>>>>>>>>>>>>>>")
    if user is not None and user.check_password(password):
        login(request, user)
        token = default_token_generator.make_token(user)
        print(user)
        return Response({'token': token}, status=status.HTTP_200_OK)
    elif user is None:
        return Response({'message': 'User with this phone number does not exist'}, status=status.HTTP_401_UNAUTHORIZED)
    else:
        return Response({'message': 'Invalid password'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAdminOrSchool])
def ngo_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = CustomUser.objects.filter(username=username).first()
    print(f"[[[[[[[[[[[[[[[[[[{user}==============")
    
    if user is not None and user.check_password(password):
        login(request, user)
        token = default_token_generator.make_token(user)
        return Response({'token': token}, status=status.HTTP_200_OK)    
    return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)