from django.shortcuts import get_object_or_404, render
from django.http import FileResponse
from rest_framework.response import Response
from rest_framework import status, views
from .serializers import ResourceSerializer
from .models import Resource

# Create your views here.
class ResourcesView(views.APIView):
    def get(self, request):
        resources = Resource.objects.all()
        serializer = ResourceSerializer(resources, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ResourceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResourceDetailView(views.APIView):
    def get(self, request, id):
        # Get a single resource by id (primary key)
        resource = get_object_or_404(Resource, id=id)
        serializer = ResourceSerializer(resource)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        # Update an existing resource
        resource = get_object_or_404(Resource, id=id)
        serializer = ResourceSerializer(resource, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        # Delete a resource
        resource = get_object_or_404(Resource, id=id)
        resource.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

class DownloadResourceView(views.APIView):
    def get(self, request, resource_id):
        resource = get_object_or_404(Resource, id=resource_id)
        return FileResponse(resource.file, as_attachment=True)