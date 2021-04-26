from django.db import models

# Create your models here.
class Visits(models.Model):
    visitor_name = models.CharField(max_length=25)
    visit_datetime = models.DateTimeField(auto_now= True)

    class Meta:
        managed = False
        db_table = 'visits'