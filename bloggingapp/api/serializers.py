from rest_framework import serializers
from .models import BlogApp


class BlogAppSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = BlogApp
        fields = ('id', 'title', 'date_created', 'date_modified','body','description')
        read_only_fields = ('date_created', 'date_modified')
