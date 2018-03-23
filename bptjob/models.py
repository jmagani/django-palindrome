from django.db import models
from django.utils import timezone

class Palindrome(models.Model):
    username = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    string   = models.CharField(max_length=200)


class BptJob(models.Model):
    name               = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    jobid              = models.CharField(max_length=200)
    userid             = models.CharField(max_length=200, default='USERJOE')
    platform           = models.CharField(max_length=200, default='LINUXR_X86')
    date_job_submitted = models.DateTimeField(
            						default=timezone.now)
    date_job_completed = models.DateTimeField(
           							blank=True, null=True)

    def get_time(self):
        self.date_job_completed = timezone.now()
        self.save()

    def __str__(self):
        return self.jobid
"""
from django.db import models
from django.utils import timezone

# Create your models here.

class BptJob(models.Model):
    #ForeignKey is a link to another DB model
	name   =  models.ForeignKey('auth.User', on_delete=models.CASCADE)
    jobid  =  models.BigIntegerField(max_value=9223372036854775807)
    userid =  models.BigIntegerField(max_value=9223372036854775807)
    platform = models.CharField(max_length=200)
    datejobsubmit = models.DateTimeField(default=timezone.now)
    datejobfinsihed = models.DateTimeField(blank=True, null=True)

	def get_time(self):
		self.published_date = timezone.now()
 		self.save()
	
	def __str__(self:
		return self.title

"""

