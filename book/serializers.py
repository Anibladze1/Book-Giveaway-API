from drf_spectacular.utils import extend_schema_field
from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    location = serializers.SerializerMethodField()

    class Meta:
        model = Book
        fields = '__all__'

    @extend_schema_field(serializers.CharField())
    def get_location(self, obj):
        return obj.book_location()
