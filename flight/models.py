from django.db import models

class airport(models.Model):
    code=models.CharField(max_length=40)
    city=models.CharField(max_length=40)

    def __str__(self):
        return f"{self.city}({self.code})"

class flight_info(models.Model):
    origin=models.ForeignKey(airport,on_delete=models.CASCADE,related_name='departure')
    destions=models.ForeignKey(airport,on_delete=models.CASCADE,related_name='arrival')
    duration=models.IntegerField()

    def __str__(self):
        return f"{self.origin} - {self.destions}"

class passengers(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    flights=models.ManyToManyField(flight_info,related_name='passenger')

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"

