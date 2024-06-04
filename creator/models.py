from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Creator(models.Model):
    """
    Model to represent creators.
    """

    user = models.ForeignKey(User, related_name='creators', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='creator/creators/')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title
