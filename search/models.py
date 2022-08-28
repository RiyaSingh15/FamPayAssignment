from django.db import models

class Videos(models.Model):
    id = models.CharField(primary_key=True, max_length=25)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=500)
    description = models.TextField()
    published_at = models.DateTimeField()
    thumbnails = models.JSONField()

    class Meta:
        db_table = 'Videos'
        indexes = [
            # Adding composite index since chances of searching description alone are less.
            models.Index(fields=['title', 'description']),
            models.Index(fields=['published_at'])
        ]

