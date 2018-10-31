from rest_framework import serializers, viewsets

from content.models import Book
from api.tag import TagSerializer
from api.category import CategorySerializer


class BookSerializer(serializers.HyperlinkedModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    # category = CategorySerializer(many=False, read_only=True)
    category = serializers.SlugRelatedField(many=False,
                                            read_only=True,
                                            slug_field='title')
    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'cover', 'tags', 'category')


class BookViewSets(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer