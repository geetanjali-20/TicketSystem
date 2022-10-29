# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from traitlets import default


class newuser(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, default = "")
	# phone = models.CharField(max_length=10)
	name= models.CharField(max_length=100)
	gender= models.CharField(
		max_length=100
	, choices=[('M','M'),('F','F')]
	)
	
	def __str__(self):
		return self.name
	
class TicketStatus(models.TextChoices):
	TO_DO = 'To Do'
	IN_PROGRESS = 'In Progress'
	IN_REVIEW = 'In Review'
	DONE = 'Done'

class registers(models.Model):
	username = models.CharField(max_length=20)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	phone = models.CharField(max_length=10)
	desc = models.TextField()
	# file = models.FileField() 
	date = models.DateField()
	
	def __str__(self):
		return self.name
	


class Ticket(models.Model):
	title = models.CharField(max_length=100)
	assignee = models.ForeignKey(User, null=True, blank = True, on_delete=models.CASCADE)
	status = models.CharField(max_length=25, choices=TicketStatus.choices, default=TicketStatus.TO_DO)
	description = models.TextField()
	created_at = models.DateTimeField('created at', auto_now_add=True)
	updated_at = models.DateTimeField('updated at', auto_now=True)