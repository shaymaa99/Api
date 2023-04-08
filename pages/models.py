from django.db import models
class Activites(models.Model):
    category=models.CharField(max_length=100)
    def __str__(self):
        return self.category
class Hoppies(models.Model):
   type=models.ForeignKey(Activites,on_delete=models.CASCADE)
   hoppy_title=models.CharField(max_length=100)
   url=models.CharField(max_length=1000)
   def __str__(self):
        return self.hoppy_title
class Book(models.Model):
    Title=models.CharField(max_length=50)
    url=models.CharField(max_length=1000)
    type=models.CharField(max_length=100)
    def __str__(self):
        return self.Title
class Video(models.Model):
    Title=models.CharField(max_length=50)
    url=models.CharField(max_length=1000)
    type=models.CharField(max_length=100)
    def __str__(self):
        return self.Title