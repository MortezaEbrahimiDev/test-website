from django.db import models

# Create your models here.
class Post(models.Model):
    # image
    # author
    title = models.CharField(max_length=200)
    content = models.TextField()
    # tag
    # category
    counted_view = models.PositiveBigIntegerField(default=0)
    status=models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(null=True)
    
    class Meta:
        ordering = ['-created_date']
    
    def __str__(self):
        return self.title