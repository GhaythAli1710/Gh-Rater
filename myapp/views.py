from django.contrib.auth.models import User
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from myapp.models import Meal, Rating
from myapp.serializers import MealSerializer, RatingSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        response = {
            'success': True,
            'data': {
                'token': token.key,
                # 'name': request.data['username']
            },
            'message': 'user register successfully'
        }
        return Response(response, status=status.HTTP_201_CREATED)
        # try:
        #     if 'username' in request.data:
        #         user = User.objects.get(username=request.data['username'], password=request.data['password'])
        #     if 'email' in request.data:
        #         user = User.objects.get(email=request.data['email'], password=request.data['password'])
        #     serializer = UserSerializer(user, many=False)
        #     token, created = Token.objects.get_or_create(user=serializer.instance)
        #     jason = {'token': token.key}
        #     return Response(jason, status=status.HTTP_200_OK)
        # except:
        #     serializer = self.get_serializer(data=request.data)
        #     serializer.is_valid(raise_exception=True)
        #     self.perform_create(serializer)
        #     token, created = Token.objects.get_or_create(user=serializer.instance)
        #     response = {'token': token.key}
        #     return Response(response, status=status.HTTP_201_CREATED)

    def list(self, request, *args, **kwargs):
        try:
            user = None
            if 'username' in request.data:
                user = User.objects.get(username=request.data['username'])
            if 'email' in request.data:
                user = User.objects.get(email=request.data['email'])
            if user.password == request.data['password']:
                serializer = UserSerializer(user, many=False)
                token, created = Token.objects.get_or_create(user=serializer.instance)
                response = {
                    'success': {
                        'token': token.key
                    }
                }
                return Response(response, status=status.HTTP_200_OK)
            return Response({'jason'}, status=status.HTTP_400_BAD_REQUEST)
        except:
            response = {'message': 'gh'}
            return Response(response, status=status.HTTP_400_BAD_REQUEST)

    '''
    update , delete , destroy , .....
    '''


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(methods=['POST'], detail=True)
    def rate_meal(self, request, pk=None):
        if 'stars' in request.data:
            '''
            create or update
            '''
            user = request.user
            meal = Meal.objects.get(id=pk)
            stars = request.data['stars']
            try:
                # update
                rating = Rating.objects.get(user=user.id, meal=meal.id)  # meal.id or pk
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                jason = {
                    'message': 'Meal rate updated',
                    'result': serializer.data
                }
                return Response(jason, status=status.HTTP_200_OK)
            except:
                # create
                rating = Rating.objects.create(stars=stars, meal=meal, user=user)
                serializer = RatingSerializer(rating, many=False)
                jason = {
                    'message': 'Meal rate created',
                    'result': serializer.data
                }
                return Response(jason, status=status.HTTP_200_OK)
        else:
            '''
            send message 
            '''
            json = {
                'message': 'stars not provided'
            }
            return Response(json, status=status.HTTP_400_BAD_REQUEST)


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        json = {
            'message': ' Invalid way to create or update '
        }
        return Response(json, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        json = {
            'message': ' Invalid way to create or update '
        }
        return Response(json, status=status.HTTP_400_BAD_REQUEST)
