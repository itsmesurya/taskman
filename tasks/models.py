from django.conf import settings
from django.urls import reverse
from django.db import models

import misaka


from django.contrib.auth import get_user_model
User = get_user_model()


class Task(models.Model):
    user = models.ForeignKey(User, related_name="tasks", on_delete=models.CASCADE)
    created_at = models.DateTimeField()
    message = models.TextField()
    message_html = models.TextField(editable=False)


    def __str__(self):
        return self.message

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse(
    #         "tasks:single",
    #         kwargs={
    #             "username": self.user.username,
    #             "pk": self.pk
    #         }
    #     )
class message(models.Model):
        message = models.TextField()

        def __str__(self):
            return self.message

        def save(self, *args, **kwargs):
            self.message_html = misaka.html(self.message)
            super().save(*args, **kwargs)

class Meta:
    ordering = ["-created_at"]
    unique_together = ['user','message']
