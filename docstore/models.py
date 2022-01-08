from django.db import models

# Create your models here.


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Folders(TimeStampMixin):

    name = models.TextField()

    size = models.IntegerField()


class Documents(TimeStampMixin):

    name = models.TextField()

    size = models.IntegerField()

    folder = models.ForeignKey("Folders", on_delete=models.SET_NULL, null=True)#need to set it to false


class Topics(TimeStampMixin):

    longDescription = models.TextField()

    shortDescription = models.CharField(max_length=50)

    document = models.ForeignKey("Documents", on_delete=models.SET_NULL, null=True)#need to set it to false

    folder = models.ForeignKey("Folders", on_delete=models.SET_NULL, null=True)#need to set it to false