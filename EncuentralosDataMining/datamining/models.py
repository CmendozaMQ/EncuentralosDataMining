from django.db import models


class scrapdata(models.Model):
    status_id = models.CharField(max_length=255)
    status_message = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    status_type = models.CharField(max_length=255)
    status_link = models.CharField(max_length=255)
    status_published = models.DateTimeField()
    found_post = models.BooleanField(default=False)



class scrapdataMessageBlank(models.Model):
    status_id = models.CharField(max_length=255)
    status_message = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    status_type = models.CharField(max_length=255)
    status_link = models.CharField(max_length=255)
    status_published = models.DateTimeField()


class savePosts(models.Model):
    status_id = models.CharField(max_length=255)
    status_message = models.CharField(max_length=255)
    link_name = models.CharField(max_length=255)
    status_type = models.CharField(max_length=255)
    status_link = models.CharField(max_length=255)
    status_published = models.DateTimeField()

    def __str__(self):
        return self.status_id

