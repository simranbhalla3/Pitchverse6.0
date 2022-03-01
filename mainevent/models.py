from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator
from team.models import Team
# Create your models here.


class CustomUserManager(BaseUserManager):
    def create_superuser(self, email, password=None):
        user = self.model(email=email, is_staff=True, is_superuser=True)
        user.set_password(password)
        user.save()
        return user

POSITION_CHOICES = ( 
    ("CEO", "CEO"), 
    ("CTO", "CTO"), 
    ("COO", "COO"), 
    ("CMO", "CMO"), 
    ("R&D", "R&D"),
)


class User(AbstractUser):
	"""docstring for User"""
	username			= None
	email 				= models.EmailField(verbose_name='Email Address', unique=True)
	name 				= models.CharField(max_length=50)
	contact_no 			= PhoneNumberField(blank=False, null=False, help_text='Add country code before the contact no.')
	roll_no				= models.CharField(max_length=100, verbose_name="Roll no/ College Name", null=False, blank=False,help_text='Enter your Roll No. if you are studying in TIET otherwise enter your college name')
	# are_you_a_thapar_student = models.BooleanField(default=True, verbose_name="Are you a thapar student?")
	alert				= models.CharField(max_length=100, default='', null=True, blank=True)
	team 				= models.ForeignKey(Team, related_name = 'team', on_delete = models.SET_NULL, null = True)
	year_of_study		= models.IntegerField(default = 0, validators=[MinValueValidator(0), MaxValueValidator(5)], null=True)
	USERNAME_FIELD 		= 'email'
	position 			= models.CharField( 
							max_length = 20, 
							choices = POSITION_CHOICES, 
							default = None,
							null = True,
							blank = True
						) 
	user_permissions 	= None
	groups 				= None
	REQUIRED_FIELDS 	= []

	objects = CustomUserManager()

	def __str__(self):
		return self.email
