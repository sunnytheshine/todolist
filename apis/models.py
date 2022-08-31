from django.db import models

class Todo(models.Model):
    id = models.BigAutoField(auto_created = True, primary_key=True)
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    deleted_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
