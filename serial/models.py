from django.db import models

class serial(models.Model):
    GENRE_CHOICE = [
        ("Drama", "Drama"),
        ("Romantic", "Romantic"),
        ("Action", "Action"),
        ("Anime", "Anime"),
        ("Horror", "Horror"),
        ("Comedy", "Comedy")

    ]
    title = models.CharField(max_length=70)
    description = models.TextField()
    image = models.ImageField(upload_to='')
    quantity = models.PositiveIntegerField()
    genre = models.CharField(max_length=70, choices=GENRE_CHOICE)
    created_date = models.DateField(auto_now_add=True)
    # upadate_date =
    duration = models.PositiveIntegerField(null= True)

    def __str__(self):
        return self.title

class SerialComment(models.Model):
    text = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    serials = models.ForeignKey(serial, on_delete=models.CASCADE,
                                related_name="serial_comment")

