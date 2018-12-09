from rest_framework import generics
from .serializers import BlogAppSerializer
from .models import BlogApp


class CreateView(generics.ListCreateAPIView):
    queryset = BlogApp.objects.all()
    serializer_class = BlogAppSerializer

    def perform_create(self, serializer):
        serializer.save()


class DetailsView(generics.RetrieveUpdateDestroyAPIView):
    """This class handles the http GET, PUT and DELETE requests."""

    queryset = BlogApp.objects.all()
    serializer_class = BlogAppSerializer