# 📚 Book Management API

A Django-based RESTful API to manage a collection of books. This app allows you to create, retrieve, update, and delete book records.

## 🔧 Features

- Add new books with title, author, ISBN, and publication date
- List all books
- Retrieve individual book details
- Update existing books
- Delete books
- Auto-recorded creation timestamp

## 📦 Model Structure

```python
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
