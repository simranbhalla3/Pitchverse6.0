from django.db import models

# Create your models here.
class Team(models.Model):
	"""docstring for Team"""
	team_name 	= models.CharField(max_length = 50) # unique
	code 		= models.CharField(max_length = 6,)
	case_study_link = models.URLField(max_length=1000, null=True,blank=True)
	case_study_name = models.CharField(max_length=50, null=True,blank=True)
	presentation	= models.FileField(upload_to = 'presentation/', default = 'competition/presentation/default.png',blank=True)
	def __str__(self):
		return self.team_name