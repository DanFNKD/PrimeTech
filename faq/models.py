from django.db import models
from django.utils.timezone import now
from django.urls import reverse

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        """Returns the absolute URL for each FAQ"""
        return reverse("faq-detail", args=[str(self.id)])

    def __str__(self):
        return self.question
