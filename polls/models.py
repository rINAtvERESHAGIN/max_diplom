from djongo import models

# Create your models here.
class TestCollection(models.Model):
    _id = models.ObjectIdField()
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    age = models.CharField(max_length=30)


class TestCollection2(models.Model):
    _id = models.ObjectIdField()
    car = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    age = models.CharField(max_length=30)


class Posts(models.Model):
    _id = models.ObjectIdField()
    post_title = models.CharField(max_length=255)
    post_description = models.TextField()
    comment = models.JSONField()
    tags = models.JSONField()
    user_details = models.JSONField()
    object = models.DjongoManager()
