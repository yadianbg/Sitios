from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from ..Serialization import SitioSerialize
from ...models import Sitio
from rest_framework import status, viewsets, generics

delete_msg = 'Sitio eliminado correctamente.'

# Metodo
@csrf_exempt
def sitio_list(request):
    if request.method == 'GET':
        queryset = Sitio.objects.all()
        serializer = SitioSerialize.SitioModelSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)


# Generic View
class SitioList(generics.ListCreateAPIView):
    queryset = Sitio.objects.all()
    serializer_class = SitioSerialize.SitioModelSerializer

class SitioDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sitio.objects.all()
    serializer_class = SitioSerialize.SitioModelSerializer
    
            
# API View (get, post)
class SitioAPI(APIView):
    def get(self, request, format=None):
        queryset = Sitio.objects.all()
        serializer = SitioSerialize.SitioModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = SitioSerialize.SitioModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# API View (get, put, delete)
class SitioAPID(APIView):
    def get(self, request, pk, format=None):
        queryset = Sitio.objects.get(id=pk)
        serializer = SitioSerialize.SitioModelSerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        serializer = SitioSerialize.SitioModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Sitio.objects.get(id=pk).delete()
        return Response(delete_msg, status=status.HTTP_200_OK)


# ViewSet
class SitioView(viewsets.ViewSet):
    def list(self, request):
        queryset = Sitio.objects.all()
        serializer = SitioSerialize.SitioModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, ):
        serializer = SitioSerialize.SitioModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Sitio.objects.get(id=pk)
        serializer = SitioSerialize.SitioModelSerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        serializer = SitioSerialize.SitioModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        Sitio.objects.get(id=pk).delete()
        return Response(delete_msg, status=status.HTTP_200_OK)


# Model ViewSet
class SitioModelView(viewsets.ModelViewSet):
    queryset = Sitio.objects.all()
    serializer_class = SitioSerialize.SitioModelSerializer