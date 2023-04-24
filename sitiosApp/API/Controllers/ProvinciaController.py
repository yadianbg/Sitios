from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from ..Serialization import ProvinciaSerialize
from ...models import Provincia
from rest_framework import status, viewsets, generics

delete_msg = 'Provincia eliminada correctamente.'

# Metodo
@csrf_exempt
def provincia_list(request):
    if request.method == 'GET':
        queryset = Provincia.objects.all()
        serializer = ProvinciaSerialize.ProvinciaModelSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


# Generic View
class ProvinciaList(generics.ListCreateAPIView):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerialize.ProvinciaModelSerializer

class ProvinciaDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerialize.ProvinciaModelSerializer
    
            
# API View (get, post)
class ProvinciaAPI(APIView):
    def get(self, request, format=None):
        queryset = Provincia.objects.all()
        serializer = ProvinciaSerialize.ProvinciaModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = ProvinciaSerialize.ProvinciaModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# API View (get, put, delete)
class ProvinciaAPID(APIView):
    def get(self, request, pk, format=None):
        queryset = Provincia.objects.get(id=pk)
        serializer = ProvinciaSerialize.ProvinciaModelSerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        serializer = ProvinciaSerialize.ProvinciaModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Provincia.objects.get(id=pk).delete()
        return Response(delete_msg, status=status.HTTP_200_OK)


# ViewSet
class ProvinciaView(viewsets.ViewSet):
    def list(self, request):
        queryset = Provincia.objects.all()
        serializer = ProvinciaSerialize.ProvinciaModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, ):
        serializer = ProvinciaSerialize.ProvinciaModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Provincia.objects.get(id=pk)
        serializer = ProvinciaSerialize.ProvinciaModelSerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        serializer = ProvinciaSerialize.ProvinciaModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        Provincia.objects.get(id=pk).delete()
        return Response(delete_msg, status=status.HTTP_200_OK)


# Model ViewSet
class ProvinciaModelView(viewsets.ModelViewSet):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerialize.ProvinciaModelSerializer