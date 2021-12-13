from rest_framework import serializers
import RK2_App.models as models


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Library
        fields = ["idlibrary", "name"]


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ["idbook", "author_name", "pages_count", "genre", "idlabrary"]