📝 Django GraphQL Blog API
A beginner-friendly Blog API built with Django + Graphene GraphQL.
Supports full CRUD for Authors and Posts with filtering by author & date.

🚀 Features
🔹 Create / Read / Update / Delete (CRUD) for Authors and Posts

🔹 GraphQL endpoint at /graphql/

🔹 Filtering posts by author and date range

🔹 Error-handled mutations with validations

🔹 SQLite3 database for development

🔹 Graphene-Django integration

🔹 Django Admin interface

🗂️ Project Structure
text
django_graphql_blog/
├── blog/                          # Blog application
│   ├── __init__.py
│   ├── admin.py                   # Django admin configuration
│   ├── apps.py                    # Blog app configuration
│   ├── models.py                  # Author and Post models
│   ├── types.py                   # GraphQL object types
│   ├── mutations.py               # Create, Update, Delete operations
│   ├── schema.py                  # App-specific GraphQL schema
│   ├── tests.py                   # Test cases
│   ├── views.py                   # Traditional Django views (if any)
│   └── migrations/                # Database migrations
│       └── __init__.py
├── blogproject/                   # Main Django project
│   ├── __init__.py
│   ├── settings.py                # Django settings
│   ├── urls.py                    # URL configuration
│   ├── schema.py                  # Root GraphQL schema
│   ├── asgi.py                    # ASGI configuration
│   └── wsgi.py                    # WSGI configuration
├── db.sqlite3                     # SQLite database (development)
├── manage.py                      # Django management script
└── README.md                      # This file
⚙️ Installation & Setup
Prerequisites
Python 3.8+

pip (Python package manager)

1. Clone or Create Project Directory
bash
# If cloning from git
git clone https://github.com/<your-username>/django_graphql_blog.git
cd django_graphql_blog

# Or if working with existing project
cd django_graphql_blog
2. Create Virtual Environment
bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python -m venv venv
source venv/bin/activate
3. Install Dependencies
Create a requirements.txt file with:

txt
Django==5.0.3
graphene-django==3.2.0
django-filter==23.5
Then install:

bash
pip install -r requirements.txt
4. Configure Database
bash
# Create migrations
python manage.py makemigrations

# Apply migrations
python manage.py migrate
5. Create Superuser (Optional)
bash
python manage.py createsuperuser
6. Run Development Server
bash
python manage.py runserver
Access Points:

🚀 GraphQL Playground: http://127.0.0.1:8000/graphql/

⚙️ Django Admin: http://127.0.0.1:8000/admin/

🔧 Configuration Files
Project Settings (blogproject/settings.py)
Make sure your settings include:

python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Third-party apps
    'graphene_django',
    
    # Local app
    'blog',
]

GRAPHENE = {
    'SCHEMA': 'blogproject.schema.schema'
}
URL Configuration (blogproject/urls.py)
python
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
📊 Data Models
Author Model
python
class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
Post Model
python
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
🔑 GraphQL API Examples
📝 MUTATIONS
Create Author
graphql
mutation {
  createAuthor(name: "John Doe", email: "john@example.com") {
    author {
      id
      name
      email
      createdAt
    }
  }
}
Create Post
graphql
mutation {
  createPost(
    title: "My First Post", 
    content: "Hello GraphQL World!", 
    authorId: 1
  ) {
    post {
      id
      title
      content
      createdAt
      author {
        name
        email
      }
    }
  }
}
Update Post
graphql
mutation {
  updatePost(
    id: 1, 
    title: "Updated Post Title", 
    content: "Updated content here"
  ) {
    post {
      id
      title
      content
      updatedAt
    }
  }
}
Delete Post
graphql
mutation {
  deletePost(id: 1) {
    success
    message
  }
}
🔍 QUERIES
Get All Posts
graphql
{
  allPosts {
    id
    title
    content
    createdAt
    author {
      id
      name
      email
    }
  }
}
Get Specific Post
graphql
{
  post(id: 1) {
    id
    title
    content
    createdAt
    author {
      name
      email
    }
  }
}
Get All Authors
graphql
{
  allAuthors {
    id
    name
    email
    createdAt
    posts {
      id
      title
    }
  }
}
Filter Posts by Author
graphql
{
  postsByAuthor(authorId: 1) {
    id
    title
    content
    createdAt
  }
}
Filter Posts by Date Range
graphql
{
  postsByDateRange(
    startDate: "2024-01-01", 
    endDate: "2024-12-31"
  ) {
    id
    title
    createdAt
    author {
      name
    }
  }
}
🎯 Available GraphQL Operations
Queries
allPosts - Retrieve all blog posts

post(id: ID!) - Get specific post by ID

allAuthors - Retrieve all authors

author(id: ID!) - Get specific author by ID

postsByAuthor(authorId: ID!) - Filter posts by author

postsByDateRange(startDate: String, endDate: String) - Filter posts by date range

Mutations
createAuthor(name: String!, email: String!) - Create new author

updateAuthor(id: ID!, name: String, email: String) - Update author

deleteAuthor(id: ID!) - Delete author

createPost(title: String!, content: String!, authorId: ID!) - Create new post

updatePost(id: ID!, title: String, content: String) - Update post

deletePost(id: ID!) - Delete post

