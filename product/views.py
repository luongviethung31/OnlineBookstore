from rest_framework import (
    generics,
    permissions,
    views
)

from .models import (
    Genre,
    Book,
    Author
)

from .serializers import (
    GenreSerializer,
    BookSerializer,
    AuthorSerializer,
    RetrieveBookSerializer,
    RetrieveGenreSerializer,
    RetrieveAuthorSerializer
)

class ListGenre(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class ListGenre(views.APIView):
    permission_classes = [permissions.AllowAny]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class ListAuthor(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class ListBook(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        return Book.objects.order_by('id')

class RetrieveBook(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Book.objects.all()
    serializer_class = RetrieveBookSerializer
    lookup_field = "slug"

class RetrieveGenre(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Genre.objects.all()
    serializer_class = RetrieveGenreSerializer
    lookup_field = "slug"

class RetrieveAuthor(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Author.objects.all()
    serializer_class = RetrieveAuthorSerializer
    lookup_field = "slug"

class CreateBook(generics.CreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UpdateBook(generics.UpdateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Book.objects.all()
    serializer_class = BookSerializer