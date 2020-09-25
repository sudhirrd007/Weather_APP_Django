from django.db import models

class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self): # show the actual city name on the deskboard
        return self.name
    
    class Meta(): # show plural of city as cities insetead of citys
        verbose_name_plural = 'cities'
