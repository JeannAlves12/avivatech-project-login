from django.db import models


class Meeting(models.Model):
    id = models.AutoField(primary_key=True)
    meeting = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    problem = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.meeting
