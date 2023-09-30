from django.db import models
from enum import Enum

from book.models import Book
from library import settings


class RequestStatus(Enum):
    PENDING = "Pending"
    ACCEPTED = "Accepted"
    DECLINED = "Declined"


class AskForBookRequest(models.Model):
    requester = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="requester")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book')
    request_date = models.DateTimeField(auto_now_add=True, blank=True)
    status = models.CharField(
        max_length=255,
        choices=[(status.value, status.name) for status in RequestStatus],
        default=RequestStatus.PENDING.value
    )

    def __str__(self):
        return f"{self.requester.username} is requesting for {self.book.title}"
