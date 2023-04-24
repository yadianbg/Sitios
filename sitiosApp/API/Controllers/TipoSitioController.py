from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from ..Serialization import TipoSitioSerialize
from ...models import TipoSitio
from rest_framework import status, viewsets, generics

delete_msg = 'Tipo de sitio eliminado correctamente.'

# Metodo
@csrf_exempt
def tipoSitio_list(request):
    if request.method == 'GET':
        queryset = TipoSitio.objects.all()
        serializer = TipoSitioSerialize.TipoSitioModelSerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
        
# API View (get, post)
class TipoSitioAPI(APIView):
    def get(self, request, format=None):
        queryset = TipoSitio.objects.all()
        serializer = TipoSitioSerialize.TipoSitioModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = TipoSitioSerialize.TipoSitioModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# API View (get, put, delete)
class TipoSitioAPID(APIView):
    def get(self, request, pk, format=None):
        queryset = TipoSitio.objects.get(id=pk)
        serializer = TipoSitioSerialize.TipoSitioModelSerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        serializer = TipoSitioSerialize.TipoSitioModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        TipoSitio.objects.get(id=pk).delete()
        return Response(delete_msg, status=status.HTTP_200_OK)


# ViewSet
class TipoSitioView(viewsets.ViewSet):
    def list(self, request):
        queryset = TipoSitio.objects.all()
        serializer = TipoSitioSerialize.TipoSitioModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, ):
        serializer = TipoSitioSerialize.TipoSitioModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = TipoSitio.objects.get(id=pk)
        serializer = TipoSitioSerialize.TipoSitioModelSerializer(queryset, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        serializer = TipoSitioSerialize.TipoSitioModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        TipoSitio.objects.get(id=pk).delete()
        return Response(delete_msg, status=status.HTTP_200_OK)


# Model ViewSet
class TipoSitioModelView(viewsets.ModelViewSet):
    queryset = TipoSitio.objects.all()
    serializer_class = TipoSitioSerialize.TipoSitioModelSerializer


# Generic View
class TipoSitioList(generics.ListCreateAPIView):
    queryset = TipoSitio.objects.all()
    serializer_class = TipoSitioSerialize.TipoSitioModelSerializer

class TipoSitioDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoSitio.objects.all()
    serializer_class = TipoSitioSerialize.TipoSitioModelSerializer