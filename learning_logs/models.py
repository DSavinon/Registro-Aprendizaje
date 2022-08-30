from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Topic(models.Model):
    """A topic the user is learnign about."""

    text = models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """Returns a string representation of the model"""
        return self.text


class Entry(models.Model):
    """Something Specific learned about the topic"""

    # on delete cascade le dice que si se borra un topic, se borren todas las entry de ese topic
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        # esto es para que se rifiera a 'Entries' cuando hay mas de un 'Entry', en un lugar de que diga 'Entrys'
        verbose_name_plural = "entries"

    def __str__(self) -> str:
        """Regresamos los primeros 50 caracteres del entry"""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        else:
            return self.text
