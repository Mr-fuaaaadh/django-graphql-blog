# 📝 Django GraphQL Blog API

A beginner-friendly **Blog API** built with **Django + Graphene GraphQL**.  
Supports full **CRUD** for Authors and Posts with filtering by author & date.

---

## 🚀 Features
- 🔹 Create / Read / Update / Delete (CRUD) for **Authors** and **Posts**
- 🔹 GraphQL endpoint at `/graphql/`
- 🔹 Filtering posts by author and date range
- 🔹 Error-handled mutations with validations
- 🔹 SQLite3 database for development

---

## 🗂️ Project Structure
django_graphql_blog/
├── blog/ # Blog app
│ ├── models.py
│ ├── types.py
│ ├── mutations.py
│ ├── schema.py
│ └── ...
├── blogproject/ # Main project folder
├── db.sqlite3
├── manage.py
└── README.md

yaml
Copy code

---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/<your-username>/django_graphql_blog.git
cd django_graphql_blog
Create virtual environment

bash
Copy code
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
Install dependencies

bash
Copy code
pip install -r requirements.txt
Run migrations

bash
Copy code
python manage.py migrate
Start the server

bash
Copy code
python manage.py runserver
Now visit 👉 http://127.0.0.1:8000/graphql/

🔑 Example GraphQL Queries
➤ Create Author
graphql
Copy code
mutation {
  createAuthor(name: "John", email: "john@example.com") {
    author { id name email }
  }
}
➤ Create Post
graphql
Copy code
mutation {
  createPost(title: "My First Post", content: "Hello GraphQL!", authorId: 1) {
    post { id title content author { name } }
  }
}
➤ Get All Posts
graphql
Copy code
{
  allPosts {
    id
    title
    author { name }
  }
}
🛠️ Tech Stack
Python 3.x

Django 5.x

Graphene-Django

SQLite (default)

📜 License
This project is open-source and available under the MIT License.