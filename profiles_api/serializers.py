from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """ Serializa un campo para probar muestro APIView """
    name = serializers.CharField(max_length=10)
