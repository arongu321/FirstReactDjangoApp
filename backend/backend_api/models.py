from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Note(models.Model):
    """
    A model representing a note.

    Attributes:
        title (CharField): The title of the note, with a maximum length of 100 characters.
        content (TextField): The content of the note.
        created_at (DateTimeField): The date and time when the note was created. Automatically set to the current date and time when the note is created.
        author (ForeignKey): A foreign key to the User model, representing the author of the note. If the user is deleted, all their notes are also deleted.
    """

    title = models.CharField(max_length=100)
    content = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        """
        Returns the string representation of the Note instance, which is the title of the note.

        Returns:
            str: The  title of the note.
        """
        return self.title
