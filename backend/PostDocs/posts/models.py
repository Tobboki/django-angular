from django.db import models
class post(models.Model):
    
    titel=models.CharField(max_length=100)
    content=models.TextField(max_length=100000)
    
    data=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.titel
