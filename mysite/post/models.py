from django.db import models

SESSION_CHOICES = (
    ('openmat', 'Open Mat'),
    ('sparring', 'Sparring'),
    ('positionalsparring', 'Positional Sparring'),
    ('drills', 'Drills'),
)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    session = models.CharField(max_length=32, choices=SESSION_CHOICES, default='drills')

    def __str__(self):
        return self.title
