from django .db import models



class Weather(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.float()
    description = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.city