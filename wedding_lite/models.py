from django.db import models

# Create your models here.
class RSVP(models.Model):
    full_name = models.CharField(max_length=100, unique=True, help_text="Enter your Full Name")
    email_address = models.EmailField(max_length=100)
    number_of_guests = models.IntegerField(choices=[(i, i) for i in range(1, 7)])
    date_of_rsvp = models.DateField(auto_now_add=True)
    message = models.TextField()
    

    class Meta:
        ordering = ['-date_of_rsvp']
        


    def __str__(self):
        return self.full_name
