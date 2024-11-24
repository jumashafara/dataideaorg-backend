from django.db import models

# Create your models here.
class Activity(models.Model):
    CATEGORY_CHOICES = [
        ('WORKSHOP', 'Workshop'),
        ('SEMINAR', 'Seminar'),
        ('TRAINING', 'Training'),
        # Add more as needed
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    completed = models.BooleanField(default=False)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, blank=True)
    url_link = models.URLField(blank=True)
    attendees = models.ManyToManyField('accounts.User', blank=True)

    def __str__(self):
        return f'{self.name} ({self.get_category_display()})'
