from django.db import models
from core import models as core_models


class Conversation(core_models.TimeStampedModel):

    participant = models.ManyToManyField("users.User", blank=True)

    def __str__(self):
        usernames = []
        for user in self.participant.all():
            usernames.append(user.username)
        return ", ".join(usernames)

    def count_msgs(self):
        return self.messages.count()

    count_msgs.short_description = "Number of Messages"

    def count_participants(self):
        return self.participant.count()

    count_participants.short_description = "Number of Participants"


class Message(core_models.TimeStampedModel):

    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user} says : {self.message}"
