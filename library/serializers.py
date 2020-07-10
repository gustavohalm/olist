from rest_framework import serializers
from .models import Author, Book


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'
        read_only_fields = ('id', )


class BookSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True, read_only=True)
    authors_id = serializers.PrimaryKeyRelatedField(source='authors', many=True, write_only=True, queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ('name', 'edition', 'publication_year', 'authors', 'authors_id')
        fields = '__all__'
        read_only_fields = ('id', )
