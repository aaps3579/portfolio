from django.db import models


# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=50)
    publication_date = models.DateTimeField(auto_now_add=True)
    body = models.TextField(max_length=500)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_format(self):
        return self.publication_date.strftime('%b %e %Y')
