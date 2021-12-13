from django.shortcuts import render
from rest_framework import viewsets
import RK2_App.models as models
import RK2_App.serializers as serializers

# Create your views here.


class LibraryViewSet(viewsets.ModelViewSet):
    queryset = models.Library.objects.all()
    serializer_class = serializers.LibrarySerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = models.Book.objects.all()
    serializer_class = serializers.BookSerializer

def getBooks(library: models.Library) -> list[models.Book]:
    result = []
    for book in models.Book.objects.all():
        if book.idlabrary == library:
            result.append(book)
    return result

def master(request):
    libraries = models.Library.objects.all()
    values = []
    for library in libraries:
        values.append((library, getBooks(library)))

    return render(request, "master.html", {"values": values })
