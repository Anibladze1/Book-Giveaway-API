from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Author, Genre, Condition
from book.permisions import IsOwnerOrAdmin
from .serializers import AuthorSerializer, GenreSerializer, ConditionSerializer
from .permisions import IsAdminOrReadOnly

# Author Views
class AuthorsListCreateView(generics.ListCreateAPIView):
    """
    API endpoint to list all authors or create a new author.

    **Permissions**:
    - Authenticated users can create a new author.
    - Everyone can view the list of authors.

    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AuthorRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint to retrieve, update, or delete an author.

    **Permissions**:
    - Only the owner or an admin can update or delete the author.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsOwnerOrAdmin]


# Genre Views
class GenresListCreateView(generics.ListCreateAPIView):
    """
    API endpoint to list all genres or create a new genre.

    **Permissions**:
    - Authenticated users can create a new genre.
    - Everyone can view the list of genres.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class GenresRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint to retrieve, update, or delete a genre.

    **Permissions**:
    - Only the owner or an admin can update or delete the genre.
    """
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [IsOwnerOrAdmin]


# Condition Views
class ConditionCreateView(generics.ListCreateAPIView):
    """
    API endpoint to create a new condition.

    **Permissions**:
    - Super users can create a new condition.
    """
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
    permission_classes = [IsAdminOrReadOnly]
