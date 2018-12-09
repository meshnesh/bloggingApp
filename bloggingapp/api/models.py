from django.db import models

class BlogApp(models.Model):
    """This class represents the blogApp model."""
    title = models.CharField(max_length=255, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    body = models.TextField()
    description = models.CharField(max_length=255)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.title)
