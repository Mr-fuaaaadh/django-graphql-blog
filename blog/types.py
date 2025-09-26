from graphene_django import DjangoObjectType
from .models import Author, Post

class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = "__all__"

class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = "__all__"