from django.db import models

class Books(models.Model):
    GENRE_CHOICE = (
        ('Comedy', 'Comedy'),
        ('Fantastic','Fantastic'),
        ('Terrible', 'Terrible'),
        ('Romantic', 'Romantic'),
        ('Drama', 'Drama'),
        ('Action', 'Action'),
        ('Education', 'Education')
    )
    title = models.CharField(max_length=50)
    description = models.TextField()
    illustration = models.ImageField(upload_to='')
    quantity = models.PositiveIntegerField()
    genre = models.CharField(max_length=10, choices=GENRE_CHOICE)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

class BookComment(models.Model):
    text = models.TextField(max_length=200, null=True)
    created_date = models.DateField(auto_now_add=True)
    books = models.ForeignKey(Books, on_delete=models.CASCADE,
                              related_name="book_comment")

