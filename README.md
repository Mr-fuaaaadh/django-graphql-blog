# 📝 Django GraphQL Blog API

A beginner-friendly **Blog API** built with **Django + Graphene GraphQL**.
Supports full **CRUD** for Authors and Posts with filtering by author & date.

---

## 🚀 Features

* 🔹 Create / Read / Update / Delete (CRUD) for **Authors** and **Posts**
* 🔹 GraphQL endpoint at `/graphql/`
* 🔹 Filtering posts by author and date range
* 🔹 Error-handled mutations with validations
* 🔹 SQLite3 database for development

---

## 🗂️ Project Structure

```
django_graphql_blog/
├── blog/                # Blog app
│   ├── models.py
│   ├── types.py
│   ├── mutations.py
│   ├── schema.py
│   └── ...
├── blogproject/         # Main project folder
├── db.sqlite3
├── manage.py
└── README.md
```

---

## ⚙️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/<your-username>/django_graphql_blog.git
cd django_graphql_blog
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate      # macOS / Linux
venv\Scripts\activate         # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run migrations**

```bash
python manage.py migrate
```

5. **Start the server**

```bash
python manage.py runserver
```

Now visit 👉 `http://127.0.0.1:8000/graphql/`

---

## 🔑 Example GraphQL Queries

### ➤ Create Author

```graphql
mutation {
  createAuthor(name: "John", email: "john@example.com") {
    author { id name email }
  }
}
```

### ➤ Create Post

```graphql
mutation {
  createPost(title: "My First Post", content: "Hello GraphQL!", authorId: 1) {
    post { id title content author { name } }
  }
}
```

### ➤ Get All Posts

```graphql
{
  allPosts {
    id
    title
    author { name }
  }
}
```

---

## 🛠️ Tech Stack

* Python 3.x
* Django 5.x
* Graphene-Django
* SQLite (default)

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgements

Built as part of a **GraphQL learning project** 🦸‍♂️
