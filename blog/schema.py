import graphene
from .models import Author, Post
from .types import AuthorType, PostType
from .mutations import Mutation as BlogMutation

class Query(graphene.ObjectType):
    all_authors = graphene.List(AuthorType)
    all_posts = graphene.List(PostType)
    post_by_id = graphene.Field(PostType, id=graphene.Int(required=True))
    posts_by_author = graphene.List(PostType, author_id=graphene.Int(required=True))
    posts_by_date = graphene.List(PostType,start_date=graphene.Date(required=True),end_date=graphene.Date(required=True))

    def resolve_all_authors(root, info):
        return Author.objects.all()

    def resolve_all_posts(root, info):
        return Post.objects.select_related("author").all()

    def resolve_post_by_id(root, info, id):
        return Post.objects.get(pk=id)
    
    def resolve_posts_by_author(root, info, author_id):
        return Post.objects.filter(author_id=author_id)
    
    def resolve_posts_by_date(root, info, start_date, end_date):
        return Post.objects.filter(created_at__date__range=(start_date, end_date))

schema = graphene.Schema(query=Query, mutation=BlogMutation)
