from rest_framework import viewsets
from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book


class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    filterset_fields = ('name',)
    paginate_by = '10'


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filterset_fields = ('name', 'publication_year', 'edition', 'authors')
    paginate_by = '10'
