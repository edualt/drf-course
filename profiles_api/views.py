from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from profiles_api import models

class HelloApiView(APIView):
    """ Clase de APIView de Prueba """

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Retornar Lista de Caracteristicas del APIView """
        an_apiview = [
                'Usamos metodos HTTP como funciones (get, post, patch, put, delete)',
                'Es similar a una vista tradicional de django',
                'Nos da el mayor control sobre la logica de nuestra aplicacion',
                'Esta mapeado manualmente a los URLs',
                ]

        return Response({'message' : 'Hello', "an_apiview" : an_apiview})

    def post(self, request):
        """ Crea un mensaje con nuestro nombre """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}, how are u?'
            return Response({'message' : message})
        else:
            return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                    )

    def put(self, request, pk=None):
        """ Maneja actualizar un objeto """

        return Response({'method' : 'PUT'})

    def patch(self, request, pk=None):
        """ Maneja actualizar parcialmente un objeto """

        return Response({'method' : 'PATCH'})

    def delete(self, request, pk=None):
        """ Maneja eliminar un objeto """

        return Response({'method' : 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Retornar Mensaje de Hola Mundo """

        a_viewset = [
                'Usa acciones (list, create, retrieve, update, partial_update)',
                'Automaticamente mapea los URLs usando Routers',
                'Provee mas funcionalidad con menos codigo'
        ]

        return Response({'message' : 'Hola!', 'a_viewset' : a_viewset})

    def create(self, request):
        """ Crear nuevo mensaje de hola mundo """

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hola {name}'
            return Response({'message' : message})
        else:
            return Response(
                    serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                    )
    
    def retrieve(self, request, pk=None):
        """ Obtiene un objeto y su ID """

        return Response({'http_method' : 'PUT'})

    def update(self, request, pk=None):
        """ Actualiza un Objeto """

        return Response({'http_method' : 'PUT'})

    def parcial_update(self, request, pk=None):
        """ Actualiza parcialmente el objeto """

        return Response({'http_method' : 'PATCH'})

    def destroy(self, request, pk=None):
        """ Destruye un objeto """

        return Response({'http_method' : 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Crear y actualizar perfiles """

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
