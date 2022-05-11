from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """ Clase de APIView de Prueba """

    def get(self, request, format=None):
        """ Retornar Lista de Caracteristicas del APIView """
        an_apiview = [
                'Usamos metodos HTTP como funciones (get, post, patch, put, delete)',
                'Es similar a una vista tradicional de django',
                'Nos da el mayor control sobre la logica de nuestra aplicacion',
                'Esta mapeado manualmente a los URLs',
                ]

        return Response({'message' : 'Hello', "an_apiview" : an_apiview})

