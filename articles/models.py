from django.db import models

# Create your models here.
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    
    
    def __str__(self):
        return self.name



class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    category=models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumb=models.ImageField(default='default.png', blank= True)
    # add in author later
    

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:100] + '...'


