from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length = 100)
    website = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.name
    
class Job(models.Model):
    STATUS_CHOICES = (
        ('considering', 'Considering'),
        ('applied', 'Applied'),
        ('network', 'Network'),
        ('phone_screen', 'Phone Screen'),
        ('interview_scheduled', 'Interview Scheduled'),
        ('offer_received', 'Offer Received'),
        ('rejected', 'Rejected')
    )

    title = models.CharField(max_length=200)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='considering')
    application_date = models.DateField()
    post_date = models.DateField()
    job_description = models.TextField()
    job_url = models.URLField(null=True, blank=True)
    feedback_tracker = models.CharField(max_length = 400)

    def __str__(self):
        return self.title

class Cover_Letter(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"Cover Letter for {self.job.title}"
    
class Resume(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"Resume for {self.job.title}"