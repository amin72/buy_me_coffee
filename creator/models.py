from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Creator(models.Model):
    """
    Model to represent creators.
    """

    user = models.OneToOneField(User, related_name='creator', on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='creator/creators/')

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.title


class Support(models.Model):
    creator = models.ForeignKey(Creator, related_name='supports', on_delete=models.CASCADE)

    amount = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    email = models.EmailField()
    cryptomus_uuid = models.UUIDField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.creator)
