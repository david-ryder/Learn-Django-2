from rest_framework import viewsets, response
from .models import Book
from .serializers import BookSerializer

# TODO: Figure this out later
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def list(self, request):
        queryset = self.queryset

        title = request.query_params.get('title', None)
        author = request.query_params.get('author', None)

        if title is not None:
            queryset = queryset.filter(title__icontains=title)

        if author is not None:
            queryset = queryset.filter(author__icontains=author)

        serializer = self.serializer_class(queryset, many=True)
        return response.Response(serializer.data)
