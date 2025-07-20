from django.db import models

class FormData(models.Model):
    name = models.CharField(max_length=100)
    table_no = models.IntegerField()
    note = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
