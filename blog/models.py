from django.db import models
from django.db.models.base import Model
from django.core.validators import MinLengthValidator

# Create your models here.

class Author(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
    email=models.EmailField()
    def full_name(self):
        return f"{self.fname} {self.lname}"
    def __str__(self):
        return self.full_name()

class Tag(models.Model):
    caption=models.CharField(max_length=50)

    def full_name(self):
        return f"{self.caption}"
    def __str__(self):
        return self.full_name()

class Post(models.Model):
    title=models.CharField(max_length=50)
    excert=models.CharField(max_length=200)
    image_name=models.ImageField(upload_to="posts")
    date=models.DateField(auto_now=True)
    slug=models.SlugField(unique=True,db_index=True)
    author=models.ForeignKey(Author,on_delete=models.SET_NULL,null=True,related_name="posts")
    content=models.TextField(validators=[MinLengthValidator])
    tag=models.ManyToManyField(Tag,related_name="tags")

    





