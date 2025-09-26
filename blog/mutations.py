import graphene
from graphene import Mutation
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from .models import Author, Post
from .types import AuthorType, PostType


# -------- Helper function --------
def get_object_or_error(model, pk, object_name="Object"):
    """
    Utility to fetch object or raise GraphQL-friendly error.
    """
    try:
        return model.objects.get(pk=pk)
    except ObjectDoesNotExist:
        raise Exception(f"{object_name} with id {pk} not found!")


# ----------------- AUTHOR MUTATIONS -----------------

class CreateAuthor(Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, name, email):
        # Validation: avoid duplicate emails
        if Author.objects.filter(email=email).exists():
            raise Exception("Author with this email already exists!")

        author = Author.objects.create(name=name, email=email)
        return CreateAuthor(author=author)


class UpdateAuthor(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        name = graphene.String()
        email = graphene.String()

    author = graphene.Field(AuthorType)

    @classmethod
    def mutate(cls, root, info, id, name=None, email=None):
        author = get_object_or_error(Author, id, "Author")

        if name:
            author.name = name
        if email:
            # Prevent duplicate email conflict
            if Author.objects.exclude(pk=id).filter(email=email).exists():
                raise Exception("Another author already uses this email!")
            author.email = email

        author.save()
        return UpdateAuthor(author=author)


class DeleteAuthor(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        author = get_object_or_error(Author, id, "Author")
        author.delete()
        return DeleteAuthor(ok=True)


# ----------------- POST MUTATIONS -----------------

class CreatePost(Mutation):
    class Arguments:
        title = graphene.String(required=True)
        content = graphene.String(required=True)
        author_id = graphene.Int(required=True)

    post = graphene.Field(PostType)

    @classmethod
    def mutate(cls, root, info, title, content, author_id):
        author = get_object_or_error(Author, author_id, "Author")
        post = Post.objects.create(title=title, content=content, author=author)
        return CreatePost(post=post)


class UpdatePost(Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        title = graphene.String()
        content = graphene.String()

    post = graphene.Field(PostType)

    @classmethod
    def mutate(cls, root, info, id, title=None, content=None):
        post = get_object_or_error(Post, id, "Post")

        if title:
            post.title = title
        if content:
            post.content = content
        post.save()

        return UpdatePost(post=post)


class DeletePost(Mutation):
    class Arguments:
        id = graphene.Int(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate(cls, root, info, id):
        post = get_object_or_error(Post, id, "Post")
        post.delete()
        return DeletePost(ok=True)


# ----------------- COMBINE ALL MUTATIONS -----------------

class Mutation(graphene.ObjectType):
    create_author = CreateAuthor.Field()
    update_author = UpdateAuthor.Field()
    delete_author = DeleteAuthor.Field()

    create_post = CreatePost.Field()
    update_post = UpdatePost.Field()
    delete_post = DeletePost.Field()
